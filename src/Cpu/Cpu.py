__author__ = 'luciano'


import threading
from src.Cpu.Interrupt import *
from src.Cpu.InterruptManager import InterruptionManager
from src.Kernel.Output import Output

class Cpu:

    def __init__(self, kernel):
        self.kernel = kernel
        self.alerter = InterruptionManager(self)
        self.output = Output()
        self.memory_admin = self.kernel.memory_admin()

    def scheduler(self):
        return self.kernel.scheduler()

    def read_burst_instruction(self, pcb):
        while True:
                instr = self.memory_admin.read_memory(pcb)
                if not None == instr:
                    instr.run(self.output)
                else:
                    self.kernel.handle_signal(KillInterruption(), pcb)
                self.output.print_all()
                self.alerter.find(pcb)

    def run(self):
        pcb = self.kernel.scheduler.get_pcb
        pass
        try:
            while True:
                self.kernel.timing()
                threading.Thread(self.read_burst_instruction, pcb)
        except (KillInterruption, TimeoutInterruption, IOInterruption, NewInterruption) as e:
            self.kernel.handle_signal(e, pcb)
        except Exception:
            self.kernel.handle_signal(WaitingInterruption(), pcb)