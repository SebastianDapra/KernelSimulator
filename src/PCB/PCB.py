__author__ = 'luciano'

from src.PCB.ProcessState import *

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

    @property
    def get_pc(self):
        return self.pc

    def sum_pc(self):
        self.pc += 1

    @property
    def get_state(self):
        return self.state

    @property
    def get_pid(self):
        return self.pid

    @property
    def set_state(self, state_new):
        self.state = state_new

    @property
    def get_priority(self):
        return self.priority

    @property
    def is_last_position(self):
        return self.pc == self.final_position

    def __cmp__(self, another_pcb):
        return self.priority.__cmp__(another_pcb.get_priority)