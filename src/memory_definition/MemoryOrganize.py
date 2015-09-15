from Frame import *
from BlockTable import *
from Page import *
from Block import *


class MemoryOrganize(object):

    def __init__(self, memory):
        self.blockTable = BlockTable()
        self.memory = memory

    def has_room_for(self, size):
        pass

    def save(self, pcb, program):
        pass

    def next_position(self, pcb):
        pass

    def next_post_free(self):
        pass

    def get_next_instruction(self, pcb):
        return self.memory.read(self.next_position(pcb))

    def delete_memory_pcb(self, pcb):
        for i in range(pcb.initial_position(), pcb.final_position()):
            self.memory.delete(i)

    def delete_memory(self, program):
        for i in program.getInstrucciones():
            self.memory.delete(i)


class ContinuousAssignation(MemoryOrganize):

    def __init__(self, memory):
        super(ContinuousAssignation, self).__init__(memory)
        self.blocks = []

    def has_room_for(self, size):
        self.compact()
        return self.memory.free_memory_to_save(size)

    def save(self, pcb, program):
        position = self.next_post_free()
        size = program.size()
        block = Block(size, pcb.pid, position, position+size)
        self.save_block(block)
        for instruction in program.getInstrucciones():
            self.memory.write(self.next_post_free(), instruction)

    def next_post_free(self):
        return self.memory.next_position

    def next_position(self, pcb):
        block = self.get_block(pcb)
        pcb.sum_pc()
        if pcb.is_last_position():
            return 1000
        return block.next_pos()

    def get_block(self, pcb):
        for i in self.blocks:
            pid = i.get_pid()
            if pid == pcb.get_pid():
                return i

    def compact(self):
        delete = []
        for i in self.blocks:
            if i.get_used():
                self.clean_information(i.get_position_initial(), i.get_position_final())
                self.reassign_block(i.get_pid, i.get_position_initial(), i.get_position_final())
                delete.append(i)
        self.delete_blocks(delete)

    def delete_blocks(self, list_delete):
        for i in list_delete:
            self.blocks.remove(i)

    def reassign_block(self, pid, posicion_ini, posicion_fin):
        con_ini = posicion_ini
        con_final = posicion_fin
        diferecia_fija = con_final - con_ini
        for i in self.blocks:
            if i.get_pid != pid:
                pos_final_actual = i.get_position_final()
                pos_inicial_actual = i.get_position_initial()
                diferencia_block = pos_final_actual - pos_inicial_actual
                self.set_position_block(con_final, con_ini, diferecia_fija, diferencia_block, i)
                self.move_information(i, pos_final_actual, pos_inicial_actual)
                self.clean_information(pos_inicial_actual, pos_final_actual)
                con_ini = i.get_position_initial
                con_final = i.get_position_final

    def clean_information(self, pos_initial, pos_final):
        for i in range(pos_initial, pos_final):
            self.memory.delete_index(i)

    def set_position_block(self, con_final, con_ini, diferecia_fija, diferencia_block, i):
        if diferencia_block == diferecia_fija:
            i.set_position_final(con_final)
            i.set_position_initial(con_ini)
        else:
            if diferencia_block > diferecia_fija:
                i.set_position_initial(con_ini)
                i.set_position_final(con_final + 1)
            else:
                i.set_position_initial(con_ini)
                i.set_position_final(con_final - 1)

    def move_information(self, block, pos_final, pos_ini):
        count = pos_ini
        for i in range(block. get_position_initial(), block.get_position_final()):
            if count >= pos_final:
                self.memory.write(self.memory.read(count), i)
                count += 1
            else:
                break

    def save_block(self, block):
        self.blocks.append(block)


# Habria que implementar Paging