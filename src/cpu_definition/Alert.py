__author__ = 'luciano'


class InstructionAlert(Exception):

    def condition_of_applicability(self, pcb, cpu):
        pass

    def alert_cpu(self, pcb, cpu, pcb_table):
        print("Ejecute"+self.__str__()+" alerta.")
        new_pcb = cpu.scheduler().get_pcb()
        new_pcb.state = ProcessState.ready
        cpu.read_burst_instruction(new_pcb)

    def message(self):
        return "I'm a " + self.__str__() + "alert!"


class KillAlert(InstructionAlert):
    def __init__(self):
        super(KillAlert, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return pcb.final_position == pcb.pc

    def alert_cpu(self, pcb, cpu, pcb_table):
        super(KillAlert, self).alert_cpu(pcb, cpu, pcb_table)
        pcb.state = ProcessState.end
        cpu.memory_admin.free(pcb) ## NO EXISTE CREALO
        pcb_table.remove(pcb)


class TimeoutAlert(InstructionAlert):
    def __init__(self):
        super(TimeoutAlert, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return True

    def alert_cpu(self, pcb, cpu, pcb_table):
        super(TimeoutAlert, self).alert_cpu(pcb, cpu, pcb_table)
        pcb.state = ProcessState.ready


class IOAlert(InstructionAlert):
    def __init__(self):
        super(IOAlert, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return pcb.next_instruction().is_io_instruction()

    def alert_cpu(self, pcb, cpu, pcb_table):
        super(IOAlert, self).alert_cpu(pcb, cpu, pcb_table)
        pcb.state = ProcessState.waiting
        # Algo mejor seria hacer algo en el medio, por ej: procesar la IOInstruction
        pcb.state = ProcessState.ready


class NewAlert(InstructionAlert):
    def __init__(self):
        super(NewAlert, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        pcb.state.equals(ProcessState.new)

    def alert_cpu(self, pcb, cpu, pcb_table):
        super(NewAlert, self).alert_cpu(pcb, cpu, pcb_table)
        pcb_table.add(pcb)
        pcb.state = ProcessState.ready


class WaitingAlert(InstructionAlert):

    def __init__(self):
        super(WaitingAlert, self).__init__()

    def condition_of_applicability(self, pcb, cpu):
        return True

    def alert_cpu(self, pcb, cpu, pcb_table):
        cpu.kernel.handle_signal(TimeoutAlert(), pcb)

