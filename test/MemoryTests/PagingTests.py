__author__ = 'luciano'

import unittest
from src.Memory.Memory import *
from src.MemoryManagment.Paging.Paging import *
from src.PCB.PCB import *


class PagingTest(unittest.TestCase):

    # Arrange
    def setUp(self):
        self.memory = Memory(50)
        self.paging_policy = Paging(self.memory, 10, None)
        self.pcb1 = PCB(0, 25, PageHolder(None))
        self.pcb2 = PCB(1, 16, PageHolder(None))

    def test_WhenIWant10PagesInAMemoryOf50Cells_ThenICanMakeThem(self):
        self.assertEqual(self.paging_policy.get_amount_of_frames(), 5)

    def test_WhenIAssignOnePCB_ThenFirstFrameIsUsed(self):
        self.paging_policy.assign_to_memory(self.pcb1)
        self.assertEquals(self.paging_policy.get_amount_of_free_frames(), 4)

    def test_WhenIAssignASecondPCB_ThenSecondFrameIsUsed(self):
        self.paging_policy.assign_to_memory(self.pcb1)
        self.paging_policy.assign_to_memory(self.pcb2)
        self.assertEquals(self.paging_policy.get_amount_of_free_frames(), 3)