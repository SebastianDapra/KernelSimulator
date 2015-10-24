__author__ = 'luciano'

from src.PCB.ProcessState import *


class InterruptionManager:

    def __init__(self, cpu):
        self.handlers = {}
        self.cpu = cpu

    def register(self,handler,a_interruption):
        self.handlers.update({a_interruption:handler})

    def manager_for(self,a_interruption):
        return self.handlers.get(a_interruption)

    @property
    def timeout_interruption_manager(self):
        return TimeoutInterruptionManager()

    '''
        Le manda el PCB?? O en la interrupcion ya viene el PCB???
        ---
        TODO: Entonces hacer un KILL en cualquier momento de la ejecucion de un proceso,
        es signal_handler valido y puede hacerse si esta en modo Kernel.


       '''


class InstructionInterruptionManager:
    def condition_of_applicability(self, pcb, cpu):
        pass

    def context_switching(self, pcb, cpu):
        print("Ejecute"+self.__str__())
        next_pcb = cpu.scheduler.next_process
        next_pcb.state = ProcessState.running
        '''
            Y como conoce el CPU al prox PCB a ejecutar?
            La CPU mantiene su PCB actual
        '''
        #cpu.read_burst_instruction(next_pcb)

    def handle_signal(self, pcb, cpu, pcb_table):
        pass

    def message(self):
        return "I'm a " + self.__str__() + "alert!"


class KillInterruptionManager(InstructionInterruptionManager):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb, cpu):
        return pcb.final_position == pcb.pc

    def handle_signal(self, pcb, cpu, pcb_table):
        super().context_switching(pcb, cpu)
        pcb.state = ProcessState.terminated
        pcb_table.remove(pcb)
        # falta que lo saquen de memoria


class TimeoutInterruptionManager(InstructionInterruptionManager):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb, cpu):
        return True

    def handle_signal(self, pcb, cpu, pcb_table):
        super().context_switching(pcb, cpu)
        pcb.state = ProcessState.ready


class IOInterruptionManager(InstructionInterruptionManager):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb, cpu):
        return pcb.next_instruction.is_io

    def handle_signal(self, pcb, cpu, pcb_table):
        super(IOInterruption, self).context_switching(pcb, cpu)
        pcb.state = ProcessState.waiting
        '''
        Cuando pasa a waiting deberia mandarse a la cola de Waiting de IO
        '''
        pcb.state = ProcessState.ready


class NewInterruptionManager(InstructionInterruptionManager):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb, cpu):
        pcb.state.equals(ProcessState.new)

    def handle_signal(self, pcb, cpu, pcb_table):
        super().context_switching(pcb, cpu)
        pcb_table.add(pcb)
        pcb.state = ProcessState.ready


class EndIOInterruptionManager(InstructionInterruptionManager):
    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb, cpu):
        pcb.state.equals(ProcessState.waiting)

    def handle_signal(self, pcb, cpu, pcb_table):
        super().context_switching(pcb, cpu)


class WaitingInterruptionManager(InstructionInterruptionManager):

    def __init__(self):
        super().__init__()

    def condition_of_applicability(self, pcb, cpu):
        return True

    def context_switching(self, pcb, cpu, pcb_table):
        #cpu.kernel.signal_handler(TimeoutInterruption(), pcb)
        pass