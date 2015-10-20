class ToyMemoryAdmin:

    def __init__(self):
        self.logical_memory = None

    def set_logical_memory(self,logical_memory):
        self.logical_memory = logical_memory

    def write_instruction(self,instruction):
        self.logical_memory.memory.append(instruction)

    def write_program(self,pcb):
        self.logical_memory.memory.write(pcb)

    def delete_program(self, pcb):
        self.logical_memory.memory.delete(pcb)

    def get_instruction_of(self,pcb):
        '''
        indirecciones al pedo !!! tenes que mirarlas.
        '''
        return self.logical_memory.memory.get_instruction_of_cell(self, pcb.get_pc(), pcb.get_pid)

