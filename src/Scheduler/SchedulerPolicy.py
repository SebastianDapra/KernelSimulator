class SchedulerPolicy:

    def __init__(self):
        pass

    def push_to_queue(self, sts, pcb):
        pass

    def send_next_to_cpu(self, scheduler):
        if self.__satisfy_conditions_of_sending(scheduler):
            process_to_cpu = scheduler.ready_queue.pop(0)
            scheduler.cpu.change_pcb(process_to_cpu)

    def __satisfy_conditions_of_sending(self,scheduler):
        return scheduler.cpu.pcb is None and scheduler.ready_queue.__len__() > 0

class FifoPolicy (SchedulerPolicy):

    def push_to_queue(self, scheduler, pcb):
        scheduler.ready_queue.append(pcb)
        scheduler.ask_cpu_for_space()


class PriorityPolicy(SchedulerPolicy):

    def push_to_queue(self, scheduler, pcb):
        self.priority_push(scheduler, pcb)
        scheduler.ask_cpu_for_space()

    def priority_push(self, scheduler, pcb):
        last_index = len(scheduler.ready_queue) - 1
        if scheduler.ready_queue:
            ''' Search in ready_queue the position to insert pcb '''
            if scheduler.ready_queue[last_index].priority > pcb.priority:
                scheduler.ready_queue.append(pcb)
            else:
                for i in scheduler.ready_queue:
                    while(i.priority < pcb.priority):
                        index_of_i = scheduler.ready_queue.index(i)
                        scheduler.ready_queue.insert(index_of_i, pcb)
        else:
            scheduler.ready_queue.append(pcb)


class SchRoundRobin(SchedulerPolicy):

    def __init__(self, policy):
        self.policy = policy

    def push_to_queue(self, sts, pcb):
        self.policy.push_to_queue(sts, pcb)