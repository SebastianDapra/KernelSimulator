from src.PCB import ProcessState


class LongTermScheduler:


    def __init__(self,short_term_scheduler=None, memory_manager=None):
        self.short_term_scheduler = short_term_scheduler
        self.memory_manager = memory_manager
        self.waiting_queue = []

    def set_short_term_scheduler(self,scheduler):
        self.short_term_scheduler = scheduler

    def send_pcb_to_sts(self, a_short_scheduler):
        if self.waiting_queue.__len__() > 0:
            first_pcb = self.waiting_queue.pop(0)
            '''
            quiero agarrar al primero
            first_pcb.setState(new Ready())
            si la cola de waiting tiene lugar deberia pasar ahi
            hacer el state con enum ?

            '''
            a_short_scheduler.push_to_queue(first_pcb)

    def handle_pcb(self, pcb, a_short_scheduler):
        self.waiting_queue.insert(0, pcb)
        if a_short_scheduler.not_full():
            self.send_pcb_to_sts(a_short_scheduler)

    def add_pcb(self,pcb,scheduler):
        pcb.set_state(1)
        scheduler.policy.add_pcb(pcb)



    def init_process(self, pcb):
        if self._memory_manager.can_serve(pcb):
            self._memory_manager.write(pcb)
            self._shortTermS.add(pcb)
        else:
            self._waitingPrograms.append(pcb)

    def init_pending_process(self, process_size):
       pcb = next(i for i in self._waitingPrograms if i.get_amount_of_instructions is process_size)
       begin = self._memory_manager.write(pcb)
       pcb.set_start_instruction(begin)
       self._shortTermS.add(pcb)

    def amount_programs_waiting(self):
        return len(self._waitingPrograms)