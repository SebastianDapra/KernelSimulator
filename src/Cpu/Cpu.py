__author__ = 'luciano'

from src.Kernel.Output import Output
from src.Cpu.Interruption import *
class Cpu:

    def __init__(self, kernel):
        self.kernel = kernel
        self.output = Output()
        self.memory_manager = None
        self.actual_pcb = None
        self.output = None

    def get_actual_pcb(self):
        return self.actual_pcb

    def set_actual_pcb(self, pcb):
        self.actual_pcb = pcb

    def set_output(self,output):
        self.output = output

    def scheduler(self):
        return self.kernel.scheduler

    def set_memory_manager(self,memory_admin):
        self.memory_manager = memory_admin

    def fetch_single_instruction(self):
        return self.memory_manager.get_instruction_of(self.actual_pcb)

    def interruption_manager(self):
        return self.kernel.get_interruption_manager()

    def execute_single_instruction(self,instruction):
        instruction.execute()
        self.actual_pcb.increment()
        if self.actual_pcb.has_finished():
            self.interruption_manager().manager_for(KillInterruption).handle_signal(self.actual_pcb,self,
                                                                                  self.kernel.pcb_table)

    def run(self):
        self.set_actual_pcb(self.kernel.scheduler.next_process())
        self.complete_instruction_cycle()

    def complete_instruction_cycle(self):
        '''
        We assume the instruction cycle to be atomic which is not necessary true
        '''
        actual_instruction = self.fetch_single_instruction()

        if actual_instruction.is_io:
            self.kernel.signal_handler(IOInterruption, self.actual_pcb)
        else:
            self.execute_single_instruction(actual_instruction)
