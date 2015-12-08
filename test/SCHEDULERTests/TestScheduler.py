from queue import PriorityQueue
import unittest

from src.Kernel.Program import Program
from src.Scheduler.Scheduler import *
from src.PCB.PCB import *
from src.Scheduler.SchedulerPolicy import *


class TestScheduler(unittest.TestCase):

    def setUp(self):
        program1 = Program('D')
        program2 = Program('E')
        program3 = Program('H')
        program4 = Program('S')

        self.pcb1 = PCB(1, 20, PageHolder(program1))
        self.pcb2 = PCB(2, 25, PageHolder(program2))
        self.pcb3 = PCB(3, 15, PageHolder(program3),PCBPriorities.MEDIUM)
        self.pcb4 = PCB(4, 6, PageHolder(program4),PCBPriorities.HIGH)
        self.scheduler = Scheduler()

    def test_scheduler_with_fifo(self):
        self.fifo = FifoPolicy(self.scheduler)
        self.fifo.add_pcb(self.pcb1)
        self.fifo.add_pcb(self.pcb2)
        self.fifo.add_pcb(self.pcb3)
        self.fifo.add_pcb(self.pcb4)
        result = self.scheduler.next_process()
        self.assertEquals(self.pcb1.get_pid, result.get_pid)

    def test_scheduler_with_round_robin(self):
        quantum = 1
        self.round_robin = RoundRobinPolicy(self.scheduler, quantum)
        self.round_robin.add_pcb(self.pcb1)
        self.round_robin.add_pcb(self.pcb2)
        self.round_robin.add_pcb(self.pcb3)
        self.round_robin.add_pcb(self.pcb4)
        expected_elements = [self.pcb1, self.pcb2, self.pcb3, self.pcb4]
        for expected_element in expected_elements:
            self.assertEqual(expected_element.get_pid, self.round_robin.next_process().get_pid)

    def test_scheduler_with_priority(self):
        self.priority_policy = PriorityPolicy(self.scheduler)
        self.priority_policy.add_pcb(self.pcb1)
        self.priority_policy.add_pcb(self.pcb2)
        self.priority_policy.add_pcb(self.pcb3)
        self.priority_policy.add_pcb(self.pcb4)
        result = self.priority_policy.next_process()
        self.assertEqual(self.pcb4, result)


