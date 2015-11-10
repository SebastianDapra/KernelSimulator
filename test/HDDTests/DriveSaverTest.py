__author__ = 'luciano'


import unittest
from src.HDD.DriveSaver import *
from src.HDD.HDD import *


class BlockCreatorTest(unittest.TestCase):

    def setUp(self):
        self.instructions = range(0, 30)
        self.otherInstructions = range(0, 25)
        hdd = HDD(10)
        self.driveSaver = hdd.get_drive_saver()

    def test_creating_a_block_with_a_list_of_30_instructions(self):
        blocks = self.driveSaver.convert_into_blocks(self.instructions)
        self.assertEqual(len(blocks), 3)

    def test_creating_a_block_with_a_list_of_25_instructions(self):
        blocks = self.driveSaver.convert_into_blocks(self.instructions)
        self.assertEqual(len(blocks), 3)

    def test_creating_a_block_with_a_list_of_30_instructions_return_3_lists_of_10(self):
        blocks = self.driveSaver.convert_into_blocks(self.instructions)
        self.assertEqual(sum(map(len, blocks)), 30)

    def test_creating_a_block_with_a_list_of_25_instructions_return_3_lists_of_10_and_1_of_5(self):
        blocks = self.driveSaver.convert_into_blocks(self.otherInstructions)
        self.assertEqual(sum(map(len, blocks)), 25)
