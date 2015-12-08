import unittest
import unittest.mock
from src.Cpu.Manager import Manager
from src.Memory.MemoryManager import MemoryManager
from src.PCB.PCBTable import PCBTable
from src.Scheduler.Scheduler import Scheduler
from src.Scheduler.SchedulerPolicy import FifoPolicy
from test.InterruptionTest.Handler_Loaders import *


class TestInterruptionHandler(unittest.TestCase):
    def setUp(self):
        self.scheduler = Scheduler()
        self.fifo_scheduler = FifoPolicy(self.scheduler)
        self.pcb_table = PCBTable()
        self.memory_manager = MemoryManager()
        self.manager = Manager(self.scheduler, self.pcb_table, self.memory_manager)
        self.interruption_manager = InterruptionHandler(self.manager)