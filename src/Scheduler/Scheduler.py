__author__ = 'luciano'
from src.Kernel.FunctionsForLists import *
'''
Me gustaria que avancemos en lo que corresponderia en la interaccion del Scheduler con el Kernel.
Tambien quisiera saber que pasa con el mismo cuando hay interrupciones
'''


class Scheduler:

    def __init__(self, policy=None, ready_queue_size=50):
        self.ready_queue = []
        self.ready_queue_size = 50
        self.policy = policy
        self.cpu = None

    def set_cpu(self, cpu):
        self.cpu = cpu

    def not_full(self):
        return self.ready_queue_size > self.ready_queue.__len__()

    def push_to_queue(self, pcb):
        self.policy.add_pcb(pcb)

    def send_next_to_cpu(self):
        self.cpu.set_actual_pcb(self.next_process())

    def ask_cpu_for_space(self):
        if self.cpu.pcb is None:
            self.send_next_to_cpu()

    def next_process(self):
        return self.policy.next_process()

    def set_as_fifo(self):
        self.policy = FifoPolicy(self.ready_queue)

    def set_as_priority(self):
        self.policy = PriorityPolicy(self.ready_queue)

    def set_as_round_robin(self, quantum):
        self.policy = RoundRobinPolicy(quantum, self.ready_queue)

    def increase_pcbs_priority(self):
        self.ready_queue = FunctionsForLists.mapList((lambda x: x.increase_priority), self.ready_queue)


class FifoPolicy:
    def __init__(self, ready_queue):
        self.readyQueue = ready_queue

    def get_readyQueue(self):
        return self.readyQueue

    def next_process(self):
        return self.readyQueue.pop(0)

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    def get_quantum(self):
        return -1


class PriorityPolicy:
    def __init__(self, ready_queue):
        self.readyQueue = ready_queue

    def next_process(self):
        return min(self.readyQueue)

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    def get_quantum(self):
        return -1


class RoundRobinPolicy:
    def __init__(self, quantum, ready_queue):
        self.readyQueue = ready_queue
        self.quantum = quantum
        self.consumed_quantum = 0

    def next_process(self):
        self.send_signal()
        return self.readyQueue.pop(0)

    def send_signal(self):
        if self.is_time_out():
            last = self.readyQueue.pop(0)
            self.reset_quantum()
            self.readyQueue.append(last)
        else:
            self.increase_quantum()

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    def increase_quantum(self):
        self.quantum += 1

    def get_quantum(self):
        return self.quantum

    def is_time_out(self):
        return self.consumed_quantum == self.quantum

    def reset_quantum(self):
        self.consumed_quantum = 0
