import unittest

from src.Cpu.InterruptionHandler import *
from src.Memory.Memory import *
from src.PCB.PCBInfoHolder import BlockHolder
from test.Helpers.TestHelper import Helper
from test.LoaderTest.ToyProgram import *
from src.Kernel.Kernel import *
from src.Scheduler.Scheduler import *
from test.InterruptionTest.Handler_Loaders import Handle_Loaders


class TestCPU(unittest.TestCase):
    def setUp(self):
        self.helper = Helper()
        self.cpu = self.helper.cpu

    def test_given_pcb_when_cpu_complete_instruction_cycle_then_the_Manager_captures_interruption(self):
        '''
        Compare the initial state of PCB's PC with final state
        '''
        self.helper.load_a_instruction_in_a_program()
        self.cpu.complete_instruction_cycle()
        self.assertEqual(1, self.cpu.actual_pcb.get_pc())

    def test_given_pcb_when_cpu_complete_instruction_cycle_then_has_IO_Interruption(self):
        self.helper.load_a_io_instruction_in_a_program()
        self.cpu.complete_instruction_cycle()
        self.assertEqual(1, self.cpu.actual_pcb.get_pc())
