__author__ = 'luciano'

from src.PCB.ProcessState import *

'''
Es candidato a pasar a ser un enum, no???
'''


class InstructionInterruption(Exception):

    def condition_of_applicability(self, pcb, cpu):
        pass

    def context_switching(self, pcb, cpu):
        next_pcb = cpu.scheduler.nextProcess
        next_pcb.state = ProcessState.running
        '''
            Y como conoce el CPU al prox PCB a ejecutar?
            La CPU mantiene su PCB actual
        '''
        #cpu.read_burst_instruction(next_pcb)

    def algo(self, pcb, cpu, pcb_table):
        pass

    def message(self):
        return "I'm a " + self.__str__() + "alert!"


class KillInterruption(InstructionInterruption):
    def __init__(self):
        super(KillInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return pcb.final_position == pcb.pc

    def algo(self, pcb, cpu, pcb_table):
        super(KillInterruption, self).context_switching(pcb, cpu)
        pcb.state = ProcessState.terminated
        pcb_table.remove(pcb)
        # falta que lo saquen de memoria


class TimeoutInterruption(InstructionInterruption):
    def __init__(self):
        super(TimeoutInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return True

    def algo(self, pcb, cpu, pcb_table):
        super(TimeoutInterruption, self).context_switching(pcb, cpu)
        pcb.state = ProcessState.ready


class IOInterruption(InstructionInterruption):
    def __init__(self):
        super(IOInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return pcb.next_instruction.is_io_instruction

    def algo(self, pcb, cpu, pcb_table):
        super(IOInterruption, self).context_switching(pcb, cpu)
        pcb.state = ProcessState.waiting
        #Podriamos hacer algo en el medio, como procesar la IOInstruction
        pcb.state = ProcessState.ready


class NewInterruption(InstructionInterruption):
    def __init__(self):
        super(NewInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        pcb.state.equals(ProcessState.new)

    def algo(self, pcb, cpu, pcb_table):
        super(NewInterruption, self).context_switching(pcb, cpu)
        pcb_table.add(pcb)
        pcb.state = ProcessState.ready


class EndIOInterruption(InstructionInterruption):
    def __init__(self):
        super(NewInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        pcb.state.equals(ProcessState.waiting)

    def algo(self, pcb, cpu, pcb_table):
        super(EndIOInterruption, self).context_switching(pcb, cpu)


class WaitingInterruption(InstructionInterruption):

    def __init__(self):
        super(WaitingInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return True

    def context_switching(self, pcb, cpu, pcb_table):
        cpu.kernel.handle_signal(TimeoutInterruption(), pcb)