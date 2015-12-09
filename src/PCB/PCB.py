from src.PCB.ProcessState import *
from src.PCB.PCBInfoHolder import *


class PCB:

    def __init__(self, pid , amount_instructions, memory_policy_for_pcb):
        self._id = pid
        self._amountInstructions = amount_instructions
        self.priority = None
        self.memory_policy_for_pcb = memory_policy_for_pcb
        self.state = None

    def set_id(self,pid):
        self._id = pid

    def __str__(self):
        return 'PCB with ID: ' + str(self._id)

    def set_amount_of_instructions(self,amountInstructions):
        self._amountInstructions = amountInstructions

    def set_base_register(self,base_register):
        self.base_register = base_register

    def get_amount_of_instructions(self):
        return self._amountInstructions

    def set_pages(self,pages):
        self.get_memory_policy_for_pcb()

    def get_pages(self):
        return self.get_memory_policy_for_pcb().get_pages()

    def get_page_assigned_by_number(self,page_number):
        return self.get_pages()[page_number]

    def get_program_name(self):
        return self.get_memory_policy_for_pcb().get_program_name()

    def get_pc(self):
        return self.memory_policy_for_pcb.current_mem_dir()

    def increment(self):
        self.memory_policy_for_pcb.increment()

    @property
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    @property
    def get_pid(self):
        return self._id

    def has_finished(self):
        return self.memory_policy_for_pcb.has_finished()

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
        return self.memory_policy_for_pcb.instructions()

    def get_memory_policy_for_pcb(self):
        return self.memory_policy_for_pcb


class PCBPriorities:

    def __init__(self):
        self._priorities = self.enum(HIGH=1, MEDIUM=2, LOW=3)

    def get_priorities(self):
        return self._priorities

    def enum(self, **enums):
        return type('Enum', (), enums)

