from queue import PriorityQueue

from src.Kernel.FunctionsForLists import FunctionsForLists
from src.Scheduler.Scheduler import Scheduler


class SchedulerPolicy:

    def __init__(self, scheduler):
        self.scheduler = scheduler
    '''
    def push_to_queue(self, sts, pcb):
        pass
    '''

    def add_pcb(self, pcb):
        self.scheduler.add_pcb(pcb)

    def next_process(self):
        return self.scheduler.next_process()
    '''
    def send_next_to_cpu(self, scheduler):
        if self.__satisfy_conditions_of_sending(scheduler):
            process_to_cpu = scheduler.ready_queue.pop(0)
            scheduler.cpu.change_pcb(process_to_cpu)

    def __satisfy_conditions_of_sending(self,scheduler):
        return scheduler.cpu.pcb is None and scheduler.ready_queue.__len__() > 0
    '''


class FifoPolicy (SchedulerPolicy):

    def __init__(self, scheduler):
        super().__init__(scheduler)

    '''
    def push_to_queue(self, scheduler, pcb):
        scheduler.ready_queue.append(pcb)
        scheduler.ask_cpu_for_space()
    '''

    def add_pcb(self, pcb):
        super().add_pcb(pcb)

    def next_process(self):
        super().next_process()


class PriorityPolicy(SchedulerPolicy):

    def __init__(self, scheduler):
        super().__init__(scheduler)
        self.priority_queue = PriorityQueue()

    def add_pcb(self, pcb): #TODO: VER TEMA PRIORIDADES DEL PCB AL AGREGAR PCB.
        self.priority_queue._put(pcb)

    def next_process(self):
        self.priority_queue._get()

    def increase_pcbs_priority(self):
        self.ready_queue = FunctionsForLists.mapList((lambda x: x.increase_priority), self.ready_queue)

    '''
    def push_to_queue(self, scheduler, pcb):
        self.priority_push(scheduler, pcb)
        scheduler.ask_cpu_for_space()

    def priority_push(self, scheduler, pcb):
        last_index = len(scheduler.ready_queue) - 1
        if scheduler.ready_queue:
            #Search in ready_queue the position to insert pcb
            if scheduler.ready_queue[last_index].priority > pcb.priority:
                scheduler.ready_queue.append(pcb)
            else:
                for i in scheduler.ready_queue:
                    while(i.priority < pcb.priority):
                        index_of_i = scheduler.ready_queue.index(i)
                        scheduler.ready_queue.insert(index_of_i, pcb)
        else:
            scheduler.ready_queue.append(pcb)
    '''


class RoundRobinPolicy(SchedulerPolicy):

    def __init__(self, scheduler, quantum):
        super().__init__(scheduler)
        self.quantum = quantum
        self.consumed_quantum = 0

    '''
    def push_to_queue(self, sts, pcb):
        self.policy.push_to_queue(sts, pcb)
    '''

    def add_pcb(self, pcb):
        super().add_pcb(pcb)

    def next_process(self):
        self.send_signal()
        return super().next_process()

    def send_signal(self): #TODO: VER
        if self.is_time_out():
            last = super().ready_queue.get(0)
            self.reset_quantum()
            super().ready_queue.put(last)
        else:
            self.increase_quantum()

    def increase_quantum(self):
        self.quantum += 1

    def is_time_out(self):
        return self.consumed_quantum == self.quantum

    def reset_quantum(self):
        self.consumed_quantum = 0