class Interruption:
    KILL = "Kill"
    NEW = "New"
    TIMEOUT = "Timeout"
    IO = "IO"
    WAITING = "Waiting"
    ENDIO = "EndIO"

    def __init__(self, pcb, interruption):
        self.pcb = pcb
        self.interruption = interruption