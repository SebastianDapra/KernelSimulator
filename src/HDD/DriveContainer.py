__author__ = 'luciano'

from src.HDD.DiskBlock import *
from random import randint
from src.HDD.DriveNavigator import Navigator


class DriveContainer:

    def __init__(self, hdd):
        self._hdd = hdd

    def __ni_idea(self,function,listM):
        return list(map(function,listM))

    def convert_into_blocks(self, instructions):
        return self.__ni_idea(lambda b: DiskBlock(b), self.split_into_blocks(instructions))

    @staticmethod
    def split_into_blocks(instructions):
        return [instructions[x:x+10] for x in range(0, len(instructions), 10)]

    def save_to_hdd(self, instructions):
        sector = randint(1, self._hdd.sectors_size())
        block_index_list = self.__ni_idea((lambda inst: self._hdd.add_block(sector, inst), self.convert_into_blocks(instructions)))
        return Navigator(self._hdd, sector, block_index_list)

