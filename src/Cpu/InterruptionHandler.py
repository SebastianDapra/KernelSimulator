from src.IO.IOManager import IOManager

from src.PCB.ProcessState import *
from src.PCB.PCB import PCB


class InterruptionHandler:

    def __init__(self, manager):
        self.manager = manager

    def handle(self, pcb, interruption):
        raise NotImplementedError


class KillInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        return pcb.final_position == pcb.pc

    def handle(self, pcb, interruption):
        super().manager.manage(pcb, interruption)

class TimeoutInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        return True

    def handle(self, pcb, interruption):
        super().manager.manage(pcb, interruption)



class IOInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        return pcb.next_instruction.is_io

    def handle(self, pcb, interruption):
        super().manager.manage(pcb, interruption)


class NewInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        pcb.state.equals(ProcessState.new)

    def handle(pcb, interruption):
        super().manager.manage(pcb, interruption)


class EndIOInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()
        self.io_manager = IOManager()

    def condition_of_applicability(self, pcb):
        pcb.state.equals(ProcessState.waiting)

    def handle(self, pcb, interruption):
        super().manager.manage(pcb, interruption)



class WaitingInterruptionHandler(InterruptionHandler):

    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        return True

    def handle(self, pcb, interruption):
        super().manager.manage(pcb, interruption)