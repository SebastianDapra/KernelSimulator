from src.HDD.DiskBlock import *
from random import randint
from src.HDD.DriveNavigator import Navigator
from src.Kernel.FunctionsForLists import *


class DriveContainer:

    def __init__(self, hdd):
        self._hdd = hdd

    def convert_into_blocks(self, instructions):
        return FunctionsForLists.mapList(lambda b: DiskBlock(b), self.split_into_blocks(instructions))

    @staticmethod
    def split_into_blocks(instructions):
        return [instructions[x:x+10] for x in range(0, len(instructions), 10)]

    def save_to_hdd(self, instructions):
        choosed_sector = randint(1, self._hdd.sectors_size())
        block_index_list = list(map(lambda inst: self._hdd.add_block(choosed_sector, inst), self.convert_into_blocks(instructions)))
        return Navigator(self._hdd, choosed_sector, block_index_list)

