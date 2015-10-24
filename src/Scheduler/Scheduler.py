__author__ = 'luciano'

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
        if self.not_full():
            self.sch_strategy.push_to_queue(self, pcb)
        self.policy.add_pcb(pcb)

    def send_next_to_cpu(self):
        self.cpu.set_actual_pcb(self.next_process())
        #self.kernel.my_long_scheduler.send_pcb_to_sts(self)
        #self.increase_pcbs_priority(1)

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
        self.ready_queue = map((lambda x: x.increase_priority), self.ready_queue)


class FifoPolicy:
    def __init__(self, ready_queue):
        self.readyQueue = ready_queue

    def get_readyQueue(self):
        return self.readyQueue

    def next_process(self):
        #if not self.readyQueue:
        #    raise Exception("No processes available!")
        return self.readyQueue.pop(0)

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    def get_quantum(self):
        return -1


class PriorityPolicy:
    def __init__(self, ready_queue):
        self.readyQueue = ready_queue

    def next_process(self):
        '''
        Aca deberia buscar al proceso con mayor prioridad y devolver ese
        '''
        return min(self.readyQueue)

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    def get_quantum(self):
        return -1


class RoundRobinPolicy:
    def __init__(self, quantum, ready_queue):
        self.readyQueue = ready_queue
        self.quantum = quantum

    def next_process(self):
        '''
        Hace FIFO pero con Quantum, mirar las diapos !!!
        '''
        return self.readyQueue.pop(0)

    def add_pcb(self, pcb):
        self.readyQueue.append(pcb)

    def get_quantum(self):
        return self.quantum


