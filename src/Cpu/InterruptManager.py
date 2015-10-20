__author__ = 'luciano'

from src.Cpu.Interrupt import *


class InterruptionManager:

    def __init__(self, cpu):
        # mover a enums !!!
        
        '''
         falta el metodo register y el handler o se wrapea en una IRQ
        :param cpu:
        :return:
        '''
        '''
        :param cpu:
        :return:
        '''
        self.alerts = [KillInterruption(), TimeoutInterruption(), IOInterruption(), NewInterruption()]
        self.cpu = cpu

    def find(self, pcb):
        #list(filter(lambda x: x.alert.condition_of_applicability(pcb, self.cpu), self.alerts))
        #filter(self.alerts)
        # esto de abajo deberia quedar mas elegante
        for alert in self.alerts:
            if alert.condition_of_applicability(pcb, self.cpu):
                return alert

    def alert_for(self, pcb):
        self.find(pcb).context_switching(pcb)


    def handle(self,interruption):
        pass

    '''
        Le manda el PCB?? O en la interrupcion ya viene el PCB???
        ---
        TODO: Entonces hacer un KILL en cualquier momento de la ejecucion de un proceso,
        es algo valido y puede hacerse si esta en modo Kernel.


       '''