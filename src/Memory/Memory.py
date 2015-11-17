__author__ = 'luciano'

import jsonpickle
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
        return self.__filter_cells(lambda x: x is None)

    def __filter_cells(self,condition):
        return list(filter(condition, self._cells))

    def __ocuppied(self):
        return self.__filter_cells(lambda x: not x is None)

    def compact(self):
        used_cells = self.__ocuppied()
        self._cells = used_cells + [None] * (len(self._cells) - len(used_cells))

    def size(self):
        return len(self._cells)