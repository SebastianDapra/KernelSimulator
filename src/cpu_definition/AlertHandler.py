__author__ = 'luciano'

class Alerter:

    def __init__(self, cpu):
        self.alerts = [KillAlert(), TimeoutAlert(), IOAlert(), NewAlert()]
        self.cpu = cpu

    def find(self, pcb):
        for alert in self.alerts:
            if alert.condition_of_applicability(pcb, self.cpu):
                return alert

    def alert_for(self, pcb):
        self.find(pcb).alert_cpu(pcb)