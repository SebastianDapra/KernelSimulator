__author__ = 'luciano'

import unittest
from src.MemoryManagment.ContinuousAssigment.Block import *


class TestBlock(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.block1 = Block(1,0,4)
        self.block2 = Block(2,5,9)
        self.block3 = Block(3,10,14)

    def test_WhenICreateANewBlock_ThenTheBlockIsFree(self):
        self.assertTrue(self.block1.isFree())

    def test_WhenISetABlockAsUser_ThenItsUsed(self):
        self.block1.setUsed()
        self.assertFalse(self.block1.isFree())

    def test_WhenIChangesABlocksIndexs_ThenTheyChange(self):
        self.block1.changeStartIndex(5)
        self.block1.changeEndIndex(9)
        self.assertEqual(self.block1._startIndex, 5)
        self.assertEqual(self.block1._endIndex, 9)

    def test_WhenIChangeNextBlockPointers_ThenIGetTheCorrectBlocks(self):
        self.block1.changeNextBlock_double(self.block2)
        self.block2.changeNextBlock_double(self.block3)
        self.assertEqual(self.block1.getNextBlock(), self.block2)
        self.assertEqual(self.block2.getNextBlock(), self.block3)
        self.assertEqual(self.block3.getPreviousBlock(), self.block2)
        self.assertEqual(self.block2.getPreviousBlock(), self.block1)

    def test_WhenIChangePreviousBlockPointers_ThenIGetTheCorrectBlocks(self):
        self.block2.changePreviousBlock_double(self.block1)
        self.block3.changePreviousBlock_double(self.block2)
        self.assertEqual(self.block1.getNextBlock(), self.block2)
        self.assertEqual(self.block2.getNextBlock(), self.block3)
        self.assertEqual(self.block3.getPreviousBlock(), self.block2)
        self.assertEqual(self.block2.getPreviousBlock(), self.block1)

