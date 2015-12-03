from threading import RLock

from src.Kernel.Kernel import *
from src.Cpu.Interruption import *


class Cpu:

    def __init__(self, kernel):
        self.kernel = kernel
        self.actual_pcb = None
        self.mutex = RLock()

    def get_actual_pcb(self):
        return self.actual_pcb

    def set_actual_pcb(self, pcb):
        self.actual_pcb = pcb

    def scheduler(self):
        return self.kernel.scheduler

    def fetch_single_instruction(self):
        return self.kernel.memory_manager.get_instruction_of(self.actual_pcb)

    def interruption_handler(self):
        return self.kernel.get_interruption_handler()

    def execute_single_instruction(self,instruction):
        instruction.execute()
        self.actual_pcb.increment()
        if self.actual_pcb.has_finished():
            self.interruption_handler().handle(Interruption(self.actual_pcb, Interruption.KILL))#TODO: ARREGLAR!
            #self.interruption_manager().manager_for(KillInterruption).handle_signal(self.actual_pcb,self,self.kernel.pcb_table)

    def run(self):
        with self.mutex:
            self.kernel.scheduler.send_next_to_cpu()
            self.complete_instruction_cycle()

    def complete_instruction_cycle(self):

        while self.kernel.mode == KernelMode(self.kernel):

            actual_instruction = self.fetch_single_instruction()

            if actual_instruction.is_io:
                self.kernel.send_signal(Interruption.IO, self.actual_pcb)
            else:
                self.execute_single_instruction(actual_instruction)