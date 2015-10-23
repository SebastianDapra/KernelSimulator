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
        self.memory_admin = None
        self.actual_pcb = None
        self.output = None

    def set_actual_pcb(self,pcb):
        self.actual_pcb = pcb

    def set_output(self,output):
        self.output = output

    def scheduler(self):
        return self.kernel.scheduler()

    def set_memory_admin(self,memory_admin):
        self.memory_admin = memory_admin

    def fetch_single_instruction(self):
        return self.memory_admin.get_instruction_of(self.actual_pcb)

    def execute_single_instruction(self,instruction):
        instruction.run()
        '''
        tiene que hacer algo mas por ahora no hago nada si es de IO, pero deberia resolver con polimorfismo
        '''

    def execute_instruction(self):
        actual_instruction = fetch_single_instruction
        while True:
            if actual_instruction is not None:
                '''
                tiene que hacer algo mas por ahora no hago nada si es de IO
                '''
                actual_instruction.run(self.output)
            else:
                self.kernel.handle_signal(KillInterruption(), self.actual_pcb)
                #self.alerter.find(self.actual_pcb)

    '''
        obteniendo el pcb del Scheduler, con cada tick del Clock (que esta en el Kernel)
        creo un Thread que lea y corra la instruccion (read_burst_instruction)
        Si es una interrupcion le digo al InterruptManager que se haga cargo



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


    '''