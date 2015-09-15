class Block:

    def __init__(self, size, pid, pos_initial, pos_final):
        self.size = size
        self.pid = pid
        self.position_initial = pos_initial
        self.position_final = pos_final
        self.position_read = pos_initial
        self.used = False

    def get_size(self):
        return self.size

    def get_used(self):
        return self.used

    def next_pos(self):
        position = self.position_read
        self.position_read += 1
        self.is_full()
        return position

    def is_full(self):
        self.used = self.position_read == self.get_position_final()

    def get_pid(self):
        return self.pid

    def get_position_initial(self):
        return self.position_initial

    def get_position_final(self):
        return self.position_final

    def set_position_final(self, position):
        self.position_final = position

    def set_position_initial(self, position):
        self.position_initial = position
