__author__ = 'luciano'

from src.PCB.ProcessState import *
from src.PCB.PCBInfoHolder import *

class PCB:

    def __init__(self, amount_instructions, pid, mem_policy):
        self._id = pid
        self._amountInstructions = amount_instructions
        self._priority = None
        self._info_holder = mem_policy

    def set_id(self,pid):
        self._id = pid

    def set_amount_of_instructions(self,amountInstructions):
        self.amountInstructions = amountInstructions

    def set_base_register(self,base_register):
        self.base_register = base_register

    def get_amount_of_instructions(self):
        return self._amountInstructions

    def get_program_name(self):
        return self.program_name

    def get_pc(self):
        return self._info_holder.current_mem_dir()

    def increment(self):
        self._info_holder.increment()

    def get_pc(self):
        return self._info_holder.current_mem_dir()

    @property
    def get_state(self):
        return self.state

    @property
    def get_pid(self):
        return self.pid

    def has_finished(self):
        return self._info_holder.has_finished()

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
        return self._info_holder.instructions()

    def __str__(self):
        return 'ID: ' + self._id

    def get_info_holder(self):
        return self._info_holder

class PCBPriorities:

    def __init__(self):
        self._priorities = self.enum(HIGH=1, MEDIUM=2, LOW=3)

    def get_priorities(self):
        return self._priorities

    def enum(self, **enums):
        return type('Enum', (), enums)

