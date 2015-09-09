__author__ = 'luciano'

class ThrowIORQ:

    def __init__(self, pcb, ioQueue, scheduler):
        self._pcb = pcb
        self._ioQueue = ioQueue
        self._scheduler = scheduler

    def handle(self):
        self._ioQueue.addToWaiting(self._pcb)

class ThrowKillRQ:

    def __init__(self, pcb, memoryManager):
        self._pcb = pcb
        self._memoryManager = memoryManager

    def handle(self):
        self._memoryManager.remove(self._pcb)

class ThrowTimeOutRQ:

    def __init__(self, pcb, scheduler):
        self._pcb = pcb
        self._scheduler = scheduler

    def handle(self):
        self._scheduler.add(self._pcb)


class BuilderInterruption:

    # Lo uso para crear a las interrupciones que necesite, se que voy a necesitar un scheduler
    def __init__(self, ioQueue, memoryManager, scheduler):
        self._ioQ = ioQueue
        self._memoryManager = memoryManager
        self._scheduler = scheduler


    def buildIORQ(self, pcb):
        return ThrowIORQ(pcb, self._ioQ)

    def buildKillRQ(self, pcb):
        return ThrowKillRQ(pcb, self._memoryManager)

    def buildTimeoutRQ(self, pcb):
        return ThrowTimeOutRQ(pcb, self._scheduler)