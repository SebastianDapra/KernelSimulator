class IOManager:

    def __init__(self):
        self.io_queue = []

    def send_to_io_queue(self, pcb, instruction):
        self.io_queue.append(instruction)