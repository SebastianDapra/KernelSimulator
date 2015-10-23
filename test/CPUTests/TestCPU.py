__author__ = 'luciano'


import unittest
from src.Memory import ToyMemory, ToyMemory_Admin
from src.PCB import PCB, PCBTable
from src.Cpu.Cpu import *
from src.Kernel import ToyProgram , Program


class TestCPU(unittest.TestCase):

    def setUp(self):
        self.memory = ToyMemory()
        self.cpu = Cpu(None)

    def load_program_in_memory(self):
        toy_program = ToyProgram(Program("Vim"))
        self.memory.write_program(toy_program.program)
        pcb = PCB(toy_program.program.instructions.size,0,None,None)
        self.cpu.set_actual_pcb(pcb)
        memory_admin = ToyMemory_Admin()
        self.cpu.set_memory_admin(memory_admin)

    def given_pcb_when_cpu_fetch_instruction_from_memory_then(self):
        self.cpu.fetch_instruction()

        self.assertEqual(3, self.pcb_table.size())

    def test_remove(self):
        self.pcb_table.remove(self.pcb2)
        self.assertEqual(2, self.pcb_table.size())

