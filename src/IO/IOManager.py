from queue import Queue

from src.IO.IODevice import IODevice


class IOManager:

    def __init__(self):
        self.waiting_io_queue = Queue()
        self.io_device = IODevice(self)

    def send_to_io_queue(self, instruction):
        self.waiting_io_queue.put(instruction)

    def send_to_ready_queue(self, pcb):
        self.io_device.send_to_ready(pcb)