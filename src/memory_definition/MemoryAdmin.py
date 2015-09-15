class MemoryAdmin:

    def __init__(self, strategy):
        self.strategy = strategy

    def __call__(self, *args, **kwargs):
        return self

    def save(self, pcb, program):
        self.strategy.save(pcb, program)

    def has_room_for(self, size):
        return self.strategy.has_room_for(size)

    def next_post_free(self):
        return self.strategy.next_post_free()

    def next_post(self, pcb):
        return self.strategy.next_position(pcb)

    def read_memory(self, pcb):
        return self.strategy.get_next_instruction(pcb)

    def free(self, pcb):
        self.strategy.delete_memory_pcb(pcb)

    def delete_memory(self, program):
        self.strategy.delete_memory(program)

