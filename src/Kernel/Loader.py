class Loader:

    def __init__(self,kernel=None):
        self.kernel = kernel
        kernel.set_loader(self)

    def load(self, memory_manager ,program):
        page_holder = self.kernel.generate_page_holder(program)
        pcb = self.kernel.create_pcb(program,page_holder)
        memory_manager.write(pcb)

    def remove(self, pcb):
        self.logical_memory.delete_program(pcb)

    def get_instructions(self,program):
        return self.hdd.get_instructions(program)