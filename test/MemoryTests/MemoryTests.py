__author__ = 'luciano'

import unittest

from src.Memory.Memory import *
from src.Instruction.Instruction import *

class MemoryTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.memory = Memory(20)
        self.instruction1 = InstructionCPU()
        self.instruction2 = InstructionIO()
        self.instruction3 = InstructionCPU()

    def test_whenTheMemoryAddsAnInstructionAndIAskForIt_thenIGetIt(self):
        self.memory.put(0, self.instruction1)
        self.memory.put(1, self.instruction2)
        self.memory.put(2, self.instruction3)
        self.assertEqual(self.memory.get(0), self.instruction1)
        self.assertEqual(self.memory.get(1), self.instruction2)
        self.assertEqual(self.memory.get(2), self.instruction3)

    def test_whenISetThreeInstructions_thenIGetTwoFreeSpaces(self):
        self.memory.put(0, self.instruction1)
        self.memory.put(1, self.instruction2)
        self.memory.put(2, self.instruction3)
        self.assertEqual(self.memory.get_free_space(), 17)

    def test_whenIHaveSomeInstructionsAndCompact_thenItAllGoesUp(self):
        for index in range(0, 5):
            self.memory.put(index, self.instruction1)
        for index in range(12, 14):
            self.memory.put(index, self.instruction2)
        for index in range(17, 20):
            self.memory.put(index, self.instruction2)
        self.memory.compact()
        self.assertEqual(self.memory.get(19), None)

