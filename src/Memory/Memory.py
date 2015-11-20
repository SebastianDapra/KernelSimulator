__author__ = 'luciano'

import jsonpickle
from src.Kernel.FunctionsForLists import *
from jsonpickle.compat import unicode

class Memory:

    def __init__(self, size):
        self._cells = [None] * size

    def read(self):
        pass

    def get_instruction_of_cell(self, index):
        return self._cells.__getitem__(index)

    def change_instruction_cell(self, from_index, to_index):
        self._cells[to_index] = self._cells[from_index]
        self._cells[from_index] = None

    def get(self, index):
        return self._cells[index]

    def put(self, position, instruction):
        self.display(position,instruction)
        self._cells[position] = instruction

    def display(self,position,instruction):
        data = self.__serialize(position,instruction)
        print("Writing in Memory Position " + data[0] + " : [ " + data[1] + " ]")

    def __serialize(self, position,instruction):
        return[jsonpickle.encode(position),jsonpickle.encode(instruction._text)]

    def get_last_index(self):
        return len(self._cells) - 1

    def get_free_space(self):
        return len(self.__not_ocuppied())

    def __not_ocuppied(self):
        return FunctionsForLists.filterList(lambda x: x is None,self._cells)

    def __ocuppied(self):
        return FunctionsForLists.filterList(lambda x: not x is None,self._cells)

    def compact(self):
        used_cells = self.__ocuppied()
        self._cells = used_cells + [None] * (len(self._cells) - len(used_cells))

    def size(self):
        return len(self._cells)