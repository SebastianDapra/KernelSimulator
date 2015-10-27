__author__ = 'luciano'

from src.PCB.ProcessState import *


class PCB:

    def __init__(self, amountInstructions, pid, priority):
        self.amountInstructions = amountInstructions
        self.pc = 0
        self.state = ProcessState.new
        self.pid = pid
        self.priority = priority
        self.base_register = None

    def set_id(self,pid):
        self.pid = pid

    def set_amount_of_instructions(self,amountInstructions):
        self.amountInstructions = amountInstructions

    def set_base_register(self,base_register):
        self.base_register = base_register

    def get_amount_of_instructions(self):
        return self.amountInstructions

    def get_program_name(self):
        return self.program_name

    def get_pc(self):
        return self.pc

    def increment(self):
        self.pc += 1

    def is_invalid(self):
        return self.pc == self.amountInstructions

    @property
    def get_state(self):
        return self.state

    @property
    def get_pid(self):
        return self.pid

    def has_finished(self):
        # Esto quizas cambia con la idea de memoria
        return self.pc == self.amountInstructions

    def set_state(self, state_new):
        self.state = state_new

    @property
    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority

    def increase_priority(self):
        if self.priority == 3:
            self.priority = PCBPriorities().get_priorities().MEDIUM
        elif self.priority == 2:
            self.priority = PCBPriorities().get_priorities().HIGH

    def __cmp__(self, another_pcb):
        return self.priority.__cmp__(another_pcb)

    def __lt__(self, other):
        return self.priority < other.priority

    def get_instructions(self):
        pass


class PCBPriorities:

    def __init__(self):
        self._priorities = self.enum(HIGH=1, MEDIUM=2, LOW=3)

    def get_priorities(self):
        return self._priorities

    def enum(self, **enums):
        return type('Enum', (), enums)