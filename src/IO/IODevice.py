import threading

from src.Cpu.Interruption import Interruption
from src.Scheduler.Scheduler import Scheduler


class IODevice(threading.Thread):

    def __init__(self, manager):
        threading.Thread.__init__(self)
        self.manager = manager
        self.instructions_to_process = []
        self.scheduler = Scheduler() or None

    def add_instruction_to_process(self):
        self.instructions_to_process.append(self.manager.waiting_io_queue.get(0))

    def process_io_instruction(self, io_instruction):
        self.instructions_to_process.remove(io_instruction)

    def send_to_ready(self, pcb):
        self.manager.manage(pcb, Interruption.ENDIO)

    def run(self):
        self.add_instruction_to_process()