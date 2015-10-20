__author__ = 'luciano'


class ToyMemory:

    def __init__(self):
        self.representacion = []

    def write(self,pcb):
        self.representacion.append(pcb)

    def delete(self,pcb):
        self.representacion.remove(pcb)

    def getNextFreePosition(self):
        return self.representacion.__sizeof__()

    def write_at(self,instruction,position):
        self.representacion.insert(position,instruction)

