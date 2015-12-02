class Interruption:
    def __init__(self, pcb, interruption):
        self.pcb = pcb
        Interruption.KILL = "Kill"
        Interruption.NEW = "New"
        Interruption.TIMEOUT = "Timeout"
        Interruption.IO = "IO"
        Interruption.WAITING = "Waiting"
        Interruption.ENDIO = "EndIO"