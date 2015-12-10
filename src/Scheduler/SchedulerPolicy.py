from queue import PriorityQueue

from src.Kernel.FunctionsForLists import FunctionsForLists
from src.Scheduler.Scheduler import Scheduler


class SchedulerPolicy:

    def __init__(self, scheduler):
        self.scheduler = scheduler

    def add_pcb(self, pcb):
        self.scheduler.add_pcb(pcb)

    def next_process(self):
        return self.scheduler.next_process()


class FifoPolicy (SchedulerPolicy):

    def __init__(self, scheduler):
        super().__init__(scheduler)

    def add_pcb(self, pcb):
        super().add_pcb(pcb)

    def next_process(self):
        super().next_process()


class PriorityPolicy(SchedulerPolicy):

    def __init__(self, scheduler):
        super().__init__(scheduler)
    '''
    def add_pcb(self, pcb): #TODO: VER TEMA PRIORIDADES DEL PCB AL AGREGAR PCB.
        super().add_pcb(pcb)
    '''

    def next_process(self):
        super().next_process()

    def increase_pcbs_priority(self):
        self.ready_queue = FunctionsForLists.mapList((lambda x: x.increase_priority), self.ready_queue)

    def add_pcb(self, pcb):
        if not self.scheduler.ready_queue.empty():
            #Search in ready_queue the position to insert pcb
            pcb_in_queue = super().next_process()

            if pcb_in_queue.priority == pcb.priority:
                super().add_pcb(pcb)
                super().add_pcb(pcb_in_queue)

            elif pcb_in_queue.priority > pcb.priority:
                super().add_pcb(pcb)
                super().add_pcb(pcb_in_queue)
            else:

                super().add_pcb(pcb_in_queue)
                super().add_pcb(pcb)
        else:
            super().add_pcb(pcb)


class RoundRobinPolicy(SchedulerPolicy):

    def __init__(self, scheduler, quantum):
        super().__init__(scheduler)
        self.quantum = quantum
        self.consumed_quantum = 0

    def add_pcb(self, pcb):
        super().add_pcb(pcb)

    def next_process(self):
        self.send_signal()
        return super().next_process()

    def send_signal(self):
        if self.is_time_out():
            last = super().next_process()
            self.reset_quantum()
            super().add_pcb(last)
        else:
            self.increase_quantum()

    def increase_quantum(self):
        self.quantum += 1

    def is_time_out(self):
        return self.consumed_quantum == self.quantum

    def reset_quantum(self):
        self.consumed_quantum = 0