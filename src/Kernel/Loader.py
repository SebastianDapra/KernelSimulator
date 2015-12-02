from src.PCB.PCBTable import PCBTable


class Loader:

    def __init__(self,kernel=None):
        self.kernel = kernel
        kernel.set_loader(self)
        self.pcb_table = PCBTable()

    def load(self, memory_manager, pcb):
        page_holder = self.kernel.generate_page_holder()
        memory_manager.write(pcb)
        self.pcb_table.add(pcb)

    def remove(self, pcb):
        self.logical_memory.delete_program(pcb)
        self.pcb_table.remove(pcb)

    def get_instructions(self,program):
        return self.hdd.get_instructions(program)