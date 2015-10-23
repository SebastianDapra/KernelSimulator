__author__ = 'luciano'


import unittest

from src.Instruction.Instruction import *
from src.Memory.ToyMemory import *
from src.Memory.ToyMemory_Admin import *
from src.PCB.PCB import *
from src.Cpu.Cpu import *
from src.Kernel.ToyProgram import *
from src.Kernel.Program import *
from src.Kernel.Output import *


class TestCPU(unittest.TestCase):

    def setUp(self):
        self.memory = ToyMemory()
        self.cpu = Cpu(None)
        self.setup_load_of_a_program_in_memory()

    def setup_load_of_a_program_in_memory(self):
        toy_program = ToyProgram(Program("Vim"))
        amount_instructions = len(toy_program.program.get_instructions())
        self.memory.write_program(toy_program.program)
        pcb = PCB(amount_instructions,1,None)
        memory_admin = ToyMemoryAdmin(self.memory)
        self.cpu.set_actual_pcb(pcb)
        self.cpu.set_memory_admin(memory_admin)

    def test_given_pcb_when_cpu_fetch_instruction_from_memory_then(self):
        instruction = self.cpu.fetch_single_instruction().text
        expected = Instruction("Hooo").text
        self.assertEqual(expected,instruction)

    def test_given_pcb_when_cpu_execute_instruction_from_memory_then(self):
        output = Output()
        instruction = self.cpu.fetch_single_instruction()
        instruction.set_output_device(output)
        self.cpu.execute_single_instruction(instruction)
        self.assertEqual(output.get(0),instruction.text)
