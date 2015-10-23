__author__ = 'luciano'

import unittest
from src.PCB.PCB import *
from src.Cpu.InterruptManager import *
from src.Cpu.Cpu import *


class TestInterruption(unittest.TestCase):

    def setUp(self):
        self.cpu = Cpu(None)
        self.interruptionManager = InterruptionManager(self.cpu)
        self.cpu.actual_pcb = PCB(3, 5,1)
        self.cpu


    def test_given_a_pcb_and_cpu_when_(self):

        self.assertEqual(3, self.pcb_table.size())

    def test_remove(self):
        self.pcb_table.remove(self.pcb2)
        self.assertEqual(2, self.pcb_table.size())

suite = unittest.TestLoader().loadTestsFromTestCase(TestInterruption)
unittest.TextTestRunner(verbosity=2).run(suite)