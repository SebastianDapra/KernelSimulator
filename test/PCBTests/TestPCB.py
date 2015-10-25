__author__ = 'luciano'

import unittest
from src.PCB.PCBTable import *
from src.PCB.PCB import *


class TestPCB(unittest.TestCase):

    def setUp(self):
        self.pcb_table = PCBTable()
        self.pcb1 = PCB(3, 5, 4)
        self.pcb2 = PCB(8, 10, 3)
        self.pcb3 = PCB(20, 30, 5)

        self.pcb_table.add(self.pcb1)
        self.pcb_table.add(self.pcb2)
        self.pcb_table.add(self.pcb3)

    def test_add(self):
        self.assertEqual(3, self.pcb_table.size())

    def test_remove(self):
        self.pcb_table.remove(self.pcb2)
        self.assertEqual(2, self.pcb_table.size())

suite = unittest.TestLoader().loadTestsFromTestCase(TestPCBTable)
unittest.TextTestRunner(verbosity=2).run(suite)