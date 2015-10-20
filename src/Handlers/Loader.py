class Loader:

    def __init__(self, hdd,logical_memory):
        self.hdd = hdd
        self.logical_memory = logical_memory

    def load(self, program):
        self.logical_memory.load_program(program)

    def remove(self, pcb):
        self.logical_memory.delete_program(pcb)

    def get_instructions(self,pcb):
        return self.hdd.get_instructions(pcb)