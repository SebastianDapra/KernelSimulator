import unittest

from src.Cpu.Clock import Clock
from src.Memory.Memory import *
from src.Scheduler.Scheduler import *
from src.Main.CpuArrangements import *
from src.PCB.PCBTable import *

class TestCPUWithClock(unittest.TestCase):
    def setUp(self):
        self.memory = Memory(50)
        self.a_kernel = Kernel(None)
        self.cpu = Cpu(self.a_kernel)
        self.scheduler = Scheduler()
        self.scheduler.set_as_fifo()
        self.clock = Clock(self.cpu)
        self.a_kernel.clock = self.clock
        self.pcb_table = PCBTable()

    def test_the_clock_makes_a_tick_and_the_cpu_fetch_a_single_instruction_to_decode(self):
        CpuArrangements().load_a_instruction_in_a_program(self.a_kernel,self.scheduler,self.pcb_table,self.cpu,self.memory)
        self.a_kernel.clock.tick()
        self.assertTrue(self.cpu.get_actual_pcb().get_pc() == 1)