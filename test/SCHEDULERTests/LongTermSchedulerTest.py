import unittest
from src.Memory.MemoryManager import MemoryManager
from src.PCB.PCB import PCB
from src.Scheduler.LongTermScheduler import LongTermScheduler
from src.Scheduler.SchedulerPolicy import Scheduler


class LongTermSchedulerTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.memory_manager = MemoryManager()
        self.memory_manager.set_policy_as_paging(3)
        self.STS = Scheduler()
        self.STS.set_as_fifo()
        self.LTS = LongTermScheduler(self.STS, self.memory_manager)
        self.pcb = PCB(0, 2049, None)
        self.pcb2 = PCB(1, 1, None)

    def test_trying_to_init_process_pcb1_and_it_pass(self):
        self.LTS.initiate_process(self.pcb2)
        self.assertEquals(1,self.LTS.amount_programs_in_long_term_scheduler(),  "Process SHOULD pass")

    def test_trying_to_init_process_pcb2_and_it_pass(self):
        self.LTS.initiate_process(self.pcb)
        self.assertEquals(1,self.LTS.amount_programs_in_long_term_scheduler(),  "Process SHOULD NOT pass")

    def releasing_process_from_waiting_queue(self):
        self.LTS.init_pending_process(1)
        self.LTS.init_pending_process(2049)
        self.assertEquals(2,self.LTS.amount_programs_in_long_term_scheduler(), "Process SHOULD pass")



