class LongTermScheduler:

    def __init__(self,short_term_scheduler, memory_manager):
        self.short_term_scheduler = short_term_scheduler or None
        self.memory_manager = memory_manager or None
        self.waiting_queue = []

    def set_short_term_scheduler(self, scheduler):
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
            a_short_scheduler.add_pcb(first_pcb)

        else:
            pass #TODO: Espera de pcbs nuevos.

    def handle_pcb(self, pcb):
        self.waiting_queue.insert(0, pcb)
        if self.short_term_scheduler.not_full():
            self.send_pcb_to_sts(self.short_term_scheduler)
    '''
    def add_pcb(self, pcb, scheduler):
        pcb.set_state(1)
        scheduler.policy.add_pcb(pcb)
    '''

    def init_process(self, pcb):
        if self.memory_manager.can_serve(pcb):
            self.memory_manager.write(pcb)
            self.short_term_scheduler.add_pcb(pcb)
        else:
            self.waiting_queue.append(pcb)

    def init_pending_process(self, process_size):
       pcb = next(i for i in self.waiting_queue if i.get_amount_of_instructions is process_size)
       begin = self.memory_manager.write(pcb)
       pcb.set_start_instruction(begin)
       self.short_term_scheduler.add_pcb(pcb)

    def amount_programs_waiting(self):
        return len(self.waiting_queue)