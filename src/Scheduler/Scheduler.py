__author__ = 'luciano'

class Scheduler:

    def __init__(self):
        self.policy = None
        self.ready_queue = []

    def __call__(self, *args, **kwargs):
        return self

    @property
    def set_as_fifo(self):
        self.policy = FifoScheduler(self.ready_queue)

    @property
    def set_as_priority(self):
        self.policy = PriorityScheduler(self.ready_queue)

    @property
    def set_as_round_robin(self, quantum):
        self.policy = RoundRobinScheduler(quantum, self.ready_queue)

    @property
    def get_pcb(self):
        return self.policy.get_pcb()

    def add_pcb(self, pcb):
        self.policy.add_pcb(pcb)

    @property
    def quantum(self):
        return self.policy.get_quantum


class FifoScheduler:
    def __init__(self, ready_queue):
        self.readyQueue = ready_queue

    @property
    def get_pcb(self):
        if not len(self.readyQueue) == 0:
            return self.readyQueue.pop(0)
        else:
            raise Exception("No processes available!")

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    @property
    def get_quantum(self):
        return 1


class PriorityScheduler():
    def __init__(self, ready_queue):
        self.readyQueue = ready_queue

    @property
    def get_pcb(self):
        return min(self.readyQueue)

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    @property
    def get_quantum(self):
        return 1


class RoundRobinScheduler():
    def __init__(self, quantum, ready_queue):
        self.readyQueue = ready_queue
        self.quantum = quantum

    @property
    def get_pcb(self):
        return self.readyQueue.pop(0)

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    @property
    def get_quantum(self):
        return self.quantum
