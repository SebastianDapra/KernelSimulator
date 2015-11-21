import unittest

from src.Kernel.Program import Program
from src.PCB.PCBTable import *
from src.PCB.PCB import *


class TestPCBInfoHolder(unittest.TestCase):

    def setUp(self):
        self.program = Program("AProgram")
        self.program.addInstruction("Hola")
        self.program.addInstruction("Chau")
        info_unit = [0, 1]
        self.block_holder = BlockHolder(self.program)
        self.block_holder.set_representation(info_unit)
        self.pcb1 = PCB(2, 1, self.block_holder)

    def test_current_memory_dir(self):
        self.assertEqual(0, self.block_holder.current_mem_dir())

    def test_i_increment_my_pc_and_ask_if_has_finished(self):
        self.block_holder.increment()
        self.assertTrue(self.block_holder.has_finished())