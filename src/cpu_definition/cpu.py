from AlertHandler import Alerter
from Alert import KillAlert, TimeoutAlert, IOAlert, NewAlert, WaitingAlert
from kernel_definition.Output import Output
import threading


class Cpu:

    def __init__(self, kernel):
        self.kernel = kernel
        self.alerter = Alerter(self)
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
                    self.kernel.handle_signal(KillAlert(), pcb)
                self.output.print_all()
                self.alerter.find(pcb)

    def run(self):
        pcb = self.kernel.scheduler.get_pcb()
        try:
            while True:
                self.kernel.timing()
                threading.Thread(self.read_burst_instruction, pcb)
        except (KillAlert, TimeoutAlert, IOAlert, NewAlert) as e:
            self.kernel.handle_signal(e, pcb)
        except Exception:
            self.kernel.handle_signal(WaitingAlert(), pcb)