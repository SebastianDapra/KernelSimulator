class Page:

    def __init__(self, index, starting_index, ending_index, amount_of_instructions):
        self._index = index
        self._amount_of_instructions = amount_of_instructions
        self._starting_index = starting_index
        self._ending_index = ending_index
        self._used = False
        self._assigned = False
        self._assigned_frame = None

    def get_index(self):
        return self._index

    def has_been_read(self,pc):
        return self.get_real_instruction_number(pc) is self._ending_index

    def set_used(self):
        self._used = True

    def has_been_used(self):
        return self._used

    def set_assigned(self):
        self._assigned = True

    def set_unassigned(self):
        self._assigned = False

    def set_frame(self, frame):
        self._assigned_frame = frame
        self.set_assigned()

    def remove_frame(self):
        self._assigned_frame = None
        self.set_unassigned()

    def get_starting_index(self):
        return self._starting_index

    def get_ending_index(self):
        return self._ending_index

    def get_amount_of_instructions(self):
        return self._amount_of_instructions

    def get_real_instruction_number(self, instruction_number):
        return self._assigned_frame.get_starting_index() + instruction_number #TODO: Check