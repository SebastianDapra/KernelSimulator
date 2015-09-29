__author__ = 'luciano'

import unittest
from src.PCB.PCB import *
from src.Scheduler.Scheduler import *

class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.pcb1 = PCB(3, 5, 20, 40, 4)
        self.pcb2 = PCB(8, 10, 25, 42, 3)
        self.pcb3 = PCB(20, 30, 15, 45, 5)
        self.pcb4 = PCB(46, 49, 5, 6, 1)

        self.scheduler = Scheduler()

    def test_scheduler_with_fifo(self):
        self.scheduler.set_as_fifo()
        self.scheduler.add_pcb(self.pcb1)
        self.scheduler.add_pcb(self.pcb2)
        self.scheduler.add_pcb(self.pcb3)
        self.scheduler.add_pcb(self.pcb4)
        result = self.scheduler.get_pcb
        self.assertEqual(self.pcb1, result)


suite = unittest.TestLoader().loadTestsFromTestCase(TestScheduler)
unittest.TextTestRunner(verbosity=2).run(suite)
