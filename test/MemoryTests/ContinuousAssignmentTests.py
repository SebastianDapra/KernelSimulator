__author__ = 'luciano'

import unittest

from src.Memory.Memory import *
from src.MemoryManagment.ContinuousAssigment.ContinuousAssignment import *
from src.MemoryManagment.ContinuousAssignment.CAPolicies import *
from src.PCB.PCB import *



class TestContinuousAssignment(unittest.TestCase):

    # Arrange
    def setUp(self):
        self.pcb1 = PCB(0, 4, BlockHolder(None))
        self.caPolicy = FirstFit()
        self.memory = Memory(20)
        self.policy = ContinuousAssignment(self.memory, self.caPolicy)

    def test_whenICreateThePolicy_thenItHasAnFreeBlock(self):
        self.assertEqual(self.policy._blocks[0].size(), 20)

    def test_whenIAddANewPCB_thenItHasTwoBlocks(self):
        self.policy.assign_to_memory(self.pcb1)
        self.assertEqual(len(self.policy._blocks), 2)

    def test_whenIAddManyPCBs_thenItHasThatManyBlocks(self):
        pcb2 = PCB(1, 2, BlockHolder(None))
        pcb3 = PCB(2, 4, BlockHolder(None))
        pcb4 = PCB(2, 4, BlockHolder(None))
        self.policy.assign_to_memory(pcb2)
        self.policy.assign_to_memory(pcb3)
        self.policy.assign_to_memory(pcb4)
        self.assertEqual(len(self.policy._blocks), 4)

    def test_whenINeedToCompact_thenItCompacts(self):
        pcb1 = PCB(0, 4, BlockHolder(None))
        pcb2 = PCB(1, 2, BlockHolder(None))
        pcb3 = PCB(2, 4, BlockHolder(None))
        pcb4 = PCB(2, 4, BlockHolder(None))
        self.policy.assign_to_memory(pcb1)
        self.policy.assign_to_memory(pcb2)
        pcb5 = PCB(3, 3, BlockHolder(None))
        self.policy.assign_to_memory(pcb5)
        self.assertEqual(len(self.policy._blocks), 4)


suite = unittest.TestLoader().loadTestsFromTestCase(TestContinuousAssignment)
unittest.TextTestRunner(verbosity=2).run(suite)
