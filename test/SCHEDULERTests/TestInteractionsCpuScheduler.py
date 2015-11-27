__author__ = 'luciano'

import unittest
from src.Scheduler.Scheduler import *
from src.Kernel.Kernel import *
from src.PCB.PCB import PCB
from queue import PriorityQueue


class TestSchedulerInteractions(unittest.TestCase):
    '''
    Testing Scheduler and CPU interactions...
    '''

    def setUp(self):
        self.pcb1 = PCB(5, 20, 4)
        self.pcb2 = PCB(4, 21, 3)
        self.a_kernel = Kernel(None)
        self.scheduler = Scheduler(None)
        self.a_kernel.set_scheduler(self.scheduler)
        self.cpu = Cpu(self.a_kernel)

    def test_when_given_scheduler_with_priority_and_cpu_then_scheduler_sends_next_process_to_cpu(self):
        queue = PriorityQueue()
        scheduler_priority = Scheduler(None, ready_queue=queue)
        self.a_kernel.set_scheduler(scheduler_priority)
        scheduler_priority.set_cpu(self.cpu)
        scheduler_priority.set_as_priority()
        self.pcb1.set_priority(1)
        scheduler_priority.push_to_queue(self.pcb1)
        self.pcb2.set_priority(2)
        scheduler_priority.push_to_queue(self.pcb2)
        expected_pcb = scheduler_priority.next_process()
        scheduler_priority.send_next_to_cpu()
        self.assertEqual(self.pcb2, self.cpu.get_actual_pcb())
        
    def test_when_given_scheduler_with_round_robin_and_a_cpu_then_scheduler_sends_next_process_to_cpu(self):
        self.scheduler.set_cpu(self.cpu)
        quantum = 1
        self.scheduler.set_as_round_robin(quantum)
        self.scheduler.push_to_queue(self.pcb1)
        self.scheduler.send_next_to_cpu()
        self.assertEqual(self.pcb1, self.cpu.get_actual_pcb())

    def test_when_given_scheduler_with_fifo_and_a_cpu_then_scheduler_sends_next_process_to_cpu(self):
        self.scheduler.set_cpu(self.cpu)
        self.scheduler.set_as_fifo()
        self.scheduler.push_to_queue(self.pcb1)
        self.scheduler.send_next_to_cpu()
        self.assertEqual(self.pcb1, self.cpu.get_actual_pcb())