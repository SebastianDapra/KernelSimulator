from src.PCB.ProcessState import *
from src.PCB.PCBInfoHolder import *


class PCB:

    def __init__(self,pid, amount_instructions,  information_about_process,priority=PCBPriorities.LOW):
        self._id = pid
        self._amountInstructions = amount_instructions
        self.priority = priority
        self.information_about_process = information_about_process
        self.state = None

    def set_id(self,pid):
        self._id = pid

    def set_amount_of_instructions(self,amountInstructions):
        self.amountInstructions = amountInstructions

    def set_base_register(self,base_register):
        self.base_register = base_register

    def get_amount_of_instructions(self):
        return self._amountInstructions

    def get_pages_assigned(self):
        return self.get_information().get_representation()

    def get_page_assigned_by_number(self,page_number):
        return self.get_pages_assigned()[page_number]

    def get_program_name(self):
        return self.information_about_process.get_program_name()

    def get_pc(self):
        return self.information_about_process.current_mem_dir()

    def increment(self):
        self.information_about_process.increment()

    @property
    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    @property
    def get_pid(self):
        return self._id

    def has_finished(self):
        return self.information_about_process.has_finished()

    @property
    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority

    def increase_priority(self):
        if self.priority == 3:
            self.priority = PCBPriorities.MEDIUM
        elif self.priority == 2:
            self.priority = PCBPriorities.HIGH

    def __cmp__(self, another_pcb):
        return self.priority.__cmp__(another_pcb)

    def __lt__(self, other):
        return self.priority < other.priority

    def get_instructions(self):
        return self.information_about_process.instructions()

    def __str__(self):
        return 'ID: ' + self._id

    def get_information(self):
        return self.information_about_process


class PCBPriorities:

    HIGH = 1
    MEDIUM = 2
    LOW = 3

    def __init__(self):
        pass

