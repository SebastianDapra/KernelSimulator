import unittest
from unittest.mock import Mock

from src.Cpu.Cpu import Cpu
from src.Kernel.Kernel import Kernel


class TestCPU(unittest.TestCase):

    def setUp(self):
        self.kernel = Mock()
        self.cpu = Cpu(self.kernel)
        self.kernel.return_value = Kernel()
        self.kernel.return_value.cpu = self.cpu
        self.memory_manager = Mock()
        self.kernel.return_value.memory_manager = self.memory_manager
        self.program = Mock()
        self.hdd = Mock()
        self.scheduler = Mock()
        self.fifo = Mock()
        self.pcb_table = Mock()

    def test_a_cpu_fetch_a_instruction_allocated_in_memory(self):
        self.helper.load_a_instruction_in_a_program()
        instruction = self.cpu.fetch_single_instruction()
        self.assertEquals(self.helper.instruction, instruction)

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
