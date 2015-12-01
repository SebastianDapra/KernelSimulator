from threading import RLock
from src.Kernel.Output import Output
from src.Cpu.Interruption import *


class Cpu:

    def __init__(self, kernel):
        self.kernel = kernel
        self.output = Output()
        self.actual_pcb = None
        self.output = None
        self.mutex = RLock()

    def get_actual_pcb(self):
        return self.actual_pcb

    def set_actual_pcb(self, pcb):
        self.actual_pcb = pcb

    def set_output(self,output):
        self.output = output

    def scheduler(self):
        return self.kernel.scheduler

    def fetch_single_instruction(self):
        return self.kernel.memory_manager.get_instruction_of(self.actual_pcb)

    def interruption_manager(self):
        return self.kernel.get_interruption_manager()

    def execute_single_instruction(self,instruction):
        instruction.execute()
        self.actual_pcb.increment()
        if self.actual_pcb.has_finished():
            self.interruption_manager().manager_for(KillInterruption).handle_signal(self.actual_pcb,self,
                                                                                  self.kernel.pcb_table)

    def run(self):
        with self.mutex:
            self.set_actual_pcb(self.kernel.scheduler.next_process())
            self.complete_instruction_cycle()

    def complete_instruction_cycle(self):

        actual_instruction = self.fetch_single_instruction()

        if actual_instruction.is_io:
            self.kernel.signal_handler(IOInterruption, self.actual_pcb)
        else:
            self.execute_single_instruction(actual_instruction)

    '''
    PROX
    '''
