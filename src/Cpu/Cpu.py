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

    def fetch_instruction(self,pcb):
        instruction = self.memory_admin.get_instruction_of(pcb)
        instruction.run()
        '''
        tiene que hacer algo mas por ahora no hago nada si es de IO, pero deberia resolver con polimorfismo
        '''

    def read_burst_instruction(self, pcb):
        while True:
                instr = self.memory_admin.read_memory(pcb)

                if not None == instr:
                    '''
                    tiene que hacer algo mas por ahora no hago nada si es de IO
                    '''
                    instr.run(self.output)
                else:
                    self.kernel.handle_signal(KillInterruption(), pcb)
                self.output.print_all()
                self.alerter.find(pcb)

    '''
        obteniendo el pcb del Scheduler, con cada tick del Clock (que esta en el Kernel)
        creo un Thread que lea y corra la instruccion (read_burst_instruction)
        Si es una interrupcion le digo al InterruptManager que se haga cargo
    '''


    def run(self):
        pcb = self.kernel.scheduler.nextProcess
        pass
        try:
            while True:
                self.kernel.timing()
                threading.Thread(self.read_burst_instruction, pcb)
        except (KillInterruption, TimeoutInterruption, IOInterruption, NewInterruption) as e:
            self.kernel.handle_signal(e, pcb)
        except Exception:
            self.kernel.handle_signal(WaitingInterruption(), pcb)