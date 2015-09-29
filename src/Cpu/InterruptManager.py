__author__ = 'luciano'

from src.Cpu.Interrupt import *

class InterruptionManager:

    def __init__(self, cpu):
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
        self.find(pcb).alert_cpu(pcb)
