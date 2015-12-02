class Interruption:
    def __init__(self, pcb, interruption):
        self.pcb = pcb
        Interruption.KILL = 1
        Interruption.NEW = 2
        Interruption.TIMEOUT = 3
        Interruption.IO = 4
        Interruption.WAITING = 5
        Interruption.ENDIO = 6