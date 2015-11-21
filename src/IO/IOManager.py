class IOManager:

    def __init__(self):
        self.waiting_io_queue = []

    def send_to_io_queue(self, instruction):
        self.waiting_io_queue.append(instruction)