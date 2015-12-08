from src.Kernel.FunctionsForLists import *


class PageHolder:

    def __init__(self,program):
        self._pc = 0
        self._pages = []
        self._current = 0
        self._policy_result = None
        self._program = program

    def increment(self):
        self._pc += 1

    def has_finished(self):
        return self._current is len(self._pages)

    def needs_reload(self, pc):
        aux = self._current
        self._current += 1
        return self._pages[aux].has_been_read(pc)

    def instructions(self):
        return self._program.get_instructions()

    def current_mem_dir(self):
        return self._pages[self._current].get_real_instruction_number(self._pc)

    def set_representation(self, information_unit):
        self._pages = information_unit

    def get_representation(self):
        return self._pages

    def get_program_name(self):
        self._program.name()

    def is_holding(self):
        '''
        TO-BE CORRECTED
        '''
        return self._pages


class BlockHolder:

    def __init__(self, program):
        self._dirs = None
        self._pc = 0
        self._program = program

    def increment(self):
        self._pc += 1

    def has_finished(self):
        return self.current_mem_dir() == self._dirs[1]

    def needs_reload(self, pc):
        return False

    def amount_instructions(self):
        return self.instructions().__len__()

    def instructions(self):
        instructions = FunctionsForLists.mapList(lambda b: b.get_data(), self._program.fetch_blocks())

        return [item for sublist in instructions for item in sublist]

    def current_mem_dir(self):
        return self._dirs[0] + self._pc

    def get_representation(self):
        return self._dirs

    def is_holding(self):
        return self._dirs is not None

    def set_representation(self, information_unit):
        self._dirs = information_unit
