__author__ = 'luciano'

import unittest
from src.Scheduler.Scheduler import *
from src.PCB.PCB import *


class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.pcb1 = PCB(3, 5, 20, 4)
        self.pcb2 = PCB(8, 10, 25, 3)
        self.pcb3 = PCB(20, 30, 15, 5)
        self.pcb4 = PCB(46, 49, 6, 1)
        self.scheduler = Scheduler(None)

    def test_scheduler_with_fifo(self):
        self.scheduler.set_as_fifo()
        self.scheduler.push_to_queue(self.pcb1)
        self.scheduler.push_to_queue(self.pcb2)
        self.scheduler.push_to_queue(self.pcb3)
        self.scheduler.push_to_queue(self.pcb4)
        result = self.scheduler.nextProcess()
        self.assertEqual(self.pcb1, result)

    def test_scheduler_with_round_robin(self):
        # Tanto este como el de abajo hay que setear bien.
        self.scheduler.set_as_round_robin()
        self.scheduler.push_to_queue(self.pcb1)
        self.scheduler.push_to_queue(self.pcb2)
        self.scheduler.push_to_queue(self.pcb3)
        self.scheduler.push_to_queue(self.pcb4)
        result = self.scheduler.nextProcess()
        self.assertEqual(self.pcb1, result)

    def test_scheduler_with_priority(self):
        self.scheduler.set_as_priority()
        self.scheduler.push_to_queue(self.pcb1)
        self.scheduler.push_to_queue(self.pcb2)
        self.scheduler.push_to_queue(self.pcb3)
        self.scheduler.push_to_queue(self.pcb4)
        result = self.scheduler.nextProcess()
        self.assertEqual(self.pcb1, result)


suite = unittest.TestLoader().loadTestsFromTestCase(TestScheduler)
unittest.TextTestRunner(verbosity=2).run(suite)
