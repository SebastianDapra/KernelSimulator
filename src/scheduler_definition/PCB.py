__author__ = 'luciano'

from ProcessState import *

class PCB:

    def __init__(self, init, fin, pc, pid, priority):
        self.init_position = init
        self.final_position = fin
        self.pc = pc
        self.state = ProcessState.new
        self.pid = pid
        self.priority = priority

    def initial_position(self):
        return self.init_position

    def final_position(self):
        return self.final_position

    def get_pc(self):
        return self.pc

    def sum_pc(self):
        self.pc += 1

    def get_state(self):
        return self.state

    def get_pid(self):
        return self.pid

    def set_state(self, state_new):
        self.state = state_new

    def get_priority(self):
        return self.priority

    def is_last_position(self):
        return self.pc == self.final_position

    def __cmp__(self, another_pcb):
        return self.priority.__cmp__(another_pcb.get_priority())