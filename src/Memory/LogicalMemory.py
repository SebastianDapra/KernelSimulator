class LogicalMemory:

    def __init__(self, memory, hdd , memory_manager):
        self.memory = memory
        self.size_of_memory = self.memory.size_of_memory
        self.id = 0
        self.hdd = hdd
        self.memory_manager = memory_manager

    def load_program(self,program):
        '''
        Esto es asqueroso pero uso del for, yugg
        '''
        for x in range(0, program.get_instructions().len + 1):
            self.memory_manager.write_instruction(x)

    def set_memory_manager(self, memory_manager):
        self.memory_manager = memory_manager

    def write_program(self, pcb):
        self.memory_manager.write_program(pcb, self)

    def delete_program(self, pcb):
        self.memory_manager.delete_program(pcb, self)

    def get_instruction_of_cell(self, pc, block_id):
        self.memory_manager.get_instruction_of_cell(pc, block_id, self)







