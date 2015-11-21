class IODevice:

    def __init__(self, manager):
        self.io_manager = manager
        self.instructions_to_process = []

    def add_instruction_to_process(self):
        self.instructions_to_process.append(self.io_manager.waiting_io_queue.pop(0))

    def process_io_instruction(self, io_instruction):
        self.instructions_to_process.remove(io_instruction)