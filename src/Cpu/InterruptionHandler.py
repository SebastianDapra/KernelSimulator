from src.IO.IOManager import IOManager

from src.PCB.ProcessState import *
from src.PCB.PCB import PCB


class InterruptionHandler:

    def __init__(self, manager):
        self.handlers = []
        self.manager = manager

    def register(self, pack):
        self.handlers.append(pack)

    def manager_for(self, a_interruption):
        for handler in self.handlers:
            if handler[0] == a_interruption:
                return handler[1]
        #return self.handlers.get(a_interruption)


    '''
        Le manda el PCB?? O en la interrupcion ya viene el PCB???
        ---
        TODO: Entonces hacer un KILL en cualquier momento de la ejecucion de un proceso,
        es signal_handler valido y puede hacerse si esta en modo Kernel.


    '''


class KillInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb, cpu):
        return pcb.final_position == pcb.pc

    def handle(self, pcb, interruption):
        super().manager.manage(pcb, interruption)

class TimeoutInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb, cpu):
        return True

    def handle(self, pcb, interruption):
        super().manager.manage(pcb, interruption)



class IOInterruptionHandler(InterruptionHandler):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb, cpu):
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

    def condition_of_applicability(self, pcb, cpu):
        pcb.state.equals(ProcessState.waiting)

    def handle(self, pcb, interruption):
        super().manager.manage(pcb, interruption)



class WaitingInterruptionHandler(InterruptionHandler):

    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb, cpu):
        return True

    def handle(self, pcb, interruption):
        super().manager.manage(pcb, interruption)