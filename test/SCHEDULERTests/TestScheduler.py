__author__ = 'luciano'

import unittest
from src.Scheduler.Scheduler import *
from src.PCB.PCB import *
import unittest.mock


class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.pcb1 = PCB(5, 20, 4)
        self.pcb2 = PCB(10, 25, 3)
        self.pcb3 = PCB(30, 15, 5)
        self.pcb4 = PCB(49, 6, 1)


    def test_scheduler_with_fifo(self):
        self.scheduler = Scheduler(None)
        self.scheduler.set_as_fifo()
        self.scheduler.push_to_queue(self.pcb1)
        self.scheduler.push_to_queue(self.pcb2)
        self.scheduler.push_to_queue(self.pcb3)
        self.scheduler.push_to_queue(self.pcb4)
        result = self.scheduler.next_process()
        self.assertEqual(self.pcb1, result)

    def test_scheduler_with_round_robin(self):
        # Tanto este como el de abajo hay que setear bien.
        self.scheduler = Scheduler(None)
        self.scheduler.set_as_round_robin(1)
        self.scheduler.push_to_queue(self.pcb1)
        self.scheduler.push_to_queue(self.pcb2)
        self.scheduler.push_to_queue(self.pcb3)
        self.scheduler.push_to_queue(self.pcb4)
        result = self.scheduler.next_process()
        self.assertEqual(self.pcb1, result)

    def test_scheduler_with_priority(self):
        self.scheduler = Scheduler(None)
        self.scheduler.set_as_priority()
        self.scheduler.push_to_queue(self.pcb1)
        self.scheduler.push_to_queue(self.pcb2)
        self.scheduler.push_to_queue(self.pcb3)
        self.scheduler.push_to_queue(self.pcb4)
        result = self.scheduler.next_process()
        self.assertEqual(self.pcb1, result)

