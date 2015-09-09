__author__ = 'luciano'

class PCB(object):

    def __init__(self, _id, amount_instructions, m_policy):
        self._id = _id
        self._amountInstructions = amount_instructions
        self._priority = None
        self._info_holder = m_policy

    def get_info_holder(self):
        return self._info_holder

    def __str__(self):
        return 'ID: ' + self._id

    def increment(self):
        self._info_holder.increment()

    def get_pc(self):
        return self._info_holder.current_mem_dir()

    def get_instructions(self):
        return self._info_holder.instructions()

    def get_amount_of_instructions(self):
        return self._amountInstructions

    def has_finished(self):
        return self._info_holder.has_finished()

    def set_priority(self, priority):
        self._priority = priority

    def increase_priority(self):
        self._priority.increasePriority()

    def decrease_priority(self):
        self._priority.decreasePriority()

class PCBPriorities:

    def __init__(self, priority_value):
        self.priority_value = priority_value

    def getPriority(self):
        return self.priority_value

    def increasePriority(self):
        if self.priority_value < 3:
            self.priority_value += 1

    def decreasePriority(self):
        if self.priority_value > 1:
            self.priority_value -= 1

class PCBCreator :

    def __init__(self):
        self._currentID = 0

    def create_pcb(self, amount_instructions, program, m_policy):
        pcb = PCB(self._currentID, amount_instructions, m_policy)
        self._currentID += 1
        return pcb