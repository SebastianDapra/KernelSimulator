from src.PCB.PCB import *

class PCBCreator :

    def __init__(self):
        self._currentID = 0

    def create_pcb(self, amount_instructions,pcb_memory_policy):
        pcb = PCB(self._currentID, amount_instructions, pcb_memory_policy)
        self._currentID += 1
        return pcb