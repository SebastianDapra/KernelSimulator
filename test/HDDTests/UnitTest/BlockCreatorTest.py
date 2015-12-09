import unittest
from src.HDD.DriveContainer import *
from src.HDD.HDD import *
from src.Instruction.Instruction import Instruction


class BlockCreatorTest(unittest.TestCase):

    def setUp(self):
        self.instructions = []
        self.otherInstructions = []
        self.load_instructions(self.instructions,30)
        self.load_instructions(self.otherInstructions,25)
        hdd = HDD(10)
        self.driveContainer = hdd.get_drive_container()

    def load_instructions(self,list,amount):
        for i in range(0, amount):
            list.append(Instruction("Hooo"))

    def test_creating_a_block_with_a_list_of_30_instructions(self):
        blocks = self.driveContainer.convert_into_blocks(self.instructions)
        for block in blocks:
            self.assertEquals(10,block.__len__())
            self.assertEquals(Instruction("Hooo").text,block.get_instructions()[0].text)
        self.assertEqual(len(blocks), 3)

    def test_creating_a_block_with_a_list_of_25_instructions(self):
        blocks = self.driveContainer.convert_into_blocks(self.instructions)
        self.assertEqual(len(blocks), 3)

    def test_creating_a_block_with_a_list_of_30_instructions_return_3_lists_of_10(self):
        blocks = self.driveContainer.convert_into_blocks(self.instructions)
        instructions_of_block = sum(map(len, blocks))
        self.assertEqual(instructions_of_block, 30)

    def test_creating_a_block_with_a_list_of_25_instructions_return_3_lists_of_10_and_1_of_5(self):
        blocks = self.driveContainer.convert_into_blocks(self.otherInstructions)
        instructions_of_block = sum(map(len, blocks))
        self.assertEqual(instructions_of_block, 25)
