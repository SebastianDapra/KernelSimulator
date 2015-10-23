class ToyMemoryAdmin:

    def __init__(self,memory):
        self.memory = memory

    def set_logical_memory(self,logical_memory):
        self.memory = logical_memory

    def write_instruction(self,instruction):
        self.memory.write_at(instruction,self.memory.getNextFreePosition())

    def write_program(self,pcb):
        self.memory.write(pcb)

    def delete_program(self, pcb):
        self.memory.delete(pcb)

    def get_instruction_of(self,pcb):
        '''
        indirecciones al pedo !!! tenes que mirarlas.
        '''
        return self.memory.get_instruction_of_cell(pcb.get_pc())

