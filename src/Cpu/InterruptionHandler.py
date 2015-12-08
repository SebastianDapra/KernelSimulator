from src.PCB.ProcessState import *


class InterruptionHandler:

    def __init__(self, manager):
        self.manager = manager or None

    def handle(self, interruption):
        raise NotImplementedError("Abstract")


class KillInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        return pcb.final_position == pcb.pc

    def handle(self, interruption):
        super().manager.manage(interruption.pcb, interruption)

class TimeoutInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        return True

    def handle(self, interruption):
        super().manager.manage(interruption.pcb, interruption)



class IOInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        return pcb.next_instruction.is_io()

    def handle(self, interruption):
        super().manager.manage(interruption.pcb, interruption)


class NewInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        pcb.state.equals(ProcessState.new)

    def handle(self, interruption):
        super().manager.manage(interruption.pcb, interruption)


class EndIOInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        pcb.state.equals(ProcessState.waiting)

    def handle(self, interruption):
        super().manager.manage(interruption.pcb, interruption)



class WaitingInterruptionHandler(InterruptionHandler):

    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb):
        return True

    def handle(self, interruption):
        super().manager.manage(interruption.pcb, interruption)