__author__ = 'luciano'

from src.PCB.ProcessState import *


class InstructionInterruption(Exception):

    def condition_of_applicability(self, pcb, cpu):
        pass

    def alert_cpu(self, pcb, cpu, pcb_table):
        print("Ejecute"+self.__str__()+" alerta.")
        new_pcb = cpu.scheduler.get_pcb
        new_pcb.state = ProcessState.ready
        cpu.read_burst_instruction(new_pcb)

    def message(self):
        return "I'm a " + self.__str__() + "alert!"


class KillInterruption(InstructionInterruption):
    def __init__(self):
        super(KillInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return pcb.final_position == pcb.pc

    def alert_cpu(self, pcb, cpu, pcb_table):
        super(KillInterruption, self).alert_cpu(pcb, cpu, pcb_table)
        pcb.state = ProcessState.end
        cpu.memory_admin.free(pcb) ## NO EXISTE CREALO
        pcb_table.remove(pcb)


class TimeoutInterruption(InstructionInterruption):
    def __init__(self):
        super(TimeoutInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return True

    def alert_cpu(self, pcb, cpu, pcb_table):
        super(TimeoutInterruption, self).alert_cpu(pcb, cpu, pcb_table)
        pcb.state = ProcessState.ready


class IOInterruption(InstructionInterruption):
    def __init__(self):
        super(IOInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return pcb.next_instruction.is_io_instruction

    def alert_cpu(self, pcb, cpu, pcb_table):
        super(IOInterruption, self).alert_cpu(pcb, cpu, pcb_table)
        pcb.state = ProcessState.waiting
        #Podriamos hacer algo en el medio, como procesar la IOInstruction
        pcb.state = ProcessState.ready


class NewInterruption(InstructionInterruption):
    def __init__(self):
        super(NewInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        pcb.state.equals(ProcessState.new)

    def alert_cpu(self, pcb, cpu, pcb_table):
        super(NewInterruption, self).alert_cpu(pcb, cpu, pcb_table)
        pcb_table.add(pcb)
        pcb.state = ProcessState.ready


class WaitingInterruption(InstructionInterruption):

    def __init__(self):
        super(WaitingInterruption, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return True

    def alert_cpu(self, pcb, cpu, pcb_table):
        cpu.kernel.handle_signal(TimeoutInterruption(), pcb)