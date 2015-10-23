__author__ = 'luciano'


class ToyMemory:

    def __init__(self):
        self.representacion = []
        self.index = 0

    def write(self,pcb):
        self.representacion.append(pcb)

    def delete(self,pcb):
        self.representacion.remove(pcb)

    def write_at(self,instruction,position):
        self.representacion.insert(position,instruction)

    def erase_instruction(self,instruction):
        self.representacion.remove(instruction)

    def write_program(self,program):
        for instruction in program.instructions:
            self.write_at(instruction,self.index)
            self.index += 1

