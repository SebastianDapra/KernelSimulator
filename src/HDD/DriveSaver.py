__author__ = 'luciano'

from src.HDD.DiskBlock import *
from random import randint
from src.HDD.DriveNavigator import Navigator


class DriveSaver:

    def __init__(self, hdd):
        self._hdd = hdd

    def convert_into_blocks(self, instructions):
        return map(lambda b: DiskBlock(b), self.split_into_blocks(instructions))

    @staticmethod
    def split_into_blocks(instructions):
        return [instructions[x:x+10] for x in xrange(0, len(instructions), 10)]

    def save_to_hdd(self, instructions):
        sector = randint(1, self._hdd.sectors_size())
        block_index_list = map(lambda inst: self._hdd.add_block(sector, inst), self.convert_into_blocks(instructions))
        return Navigator(self._hdd, sector, block_index_list)

