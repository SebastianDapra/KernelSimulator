__author__ = 'luciano'

class PCBTable:

    def __init__(self):
        self.pcbs = []

    def remove(self, pcb):
        self.pcbs.remove(pcb)

    def add(self, pcb):
        self.pcbs.append(pcb)

    def size(self):
        return self.pcbs.__len__()