from queue import PriorityQueue
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
        self.scheduler = Scheduler(None)
        quantum = 1
        self.scheduler.set_as_round_robin(quantum)
        self.scheduler.push_to_queue(self.pcb1)
        self.scheduler.push_to_queue(self.pcb2)
        self.scheduler.push_to_queue(self.pcb3)
        self.scheduler.push_to_queue(self.pcb4)
        expected_elements = [self.pcb1, self.pcb2, self.pcb3, self.pcb4]
        for expected_element in expected_elements:
            self.assertEqual(expected_element, self.scheduler.next_process())

    def test_scheduler_with_priority(self):
        queue = PriorityQueue()
        self.scheduler = Scheduler(None,ready_queue=queue)
        self.scheduler.set_as_priority()
        self.pcb1.set_priority(4)
        self.scheduler.push_to_queue(self.pcb1)
        self.pcb2.set_priority(3)
        self.scheduler.push_to_queue(self.pcb2)
        self.pcb3.set_priority(2)
        self.scheduler.push_to_queue(self.pcb3)
        self.pcb4.set_priority(1)
        self.scheduler.push_to_queue(self.pcb4)
        result = self.scheduler.next_process()
        self.assertEqual(self.pcb4, result)


