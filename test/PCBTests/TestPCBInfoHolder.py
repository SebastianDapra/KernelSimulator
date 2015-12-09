import unittest
from src.Instruction.Instruction import Instruction

from src.Kernel.Program import Program
from src.MemoryManagment.Paging.PageCreator import PageCreator
from src.PCB.PCB import *


class TestPCBInfoHolder(unittest.TestCase):

    def setUp(self):
        self.program = Program("AProgram")
        self.program.addInstruction(Instruction("Hola"))
        self.program.addInstruction(Instruction("Chau"))
        self.page_holder = PageHolder(self.program)
        self.pcb = PCB(0, 2, self.page_holder)
        self.page_creator = PageCreator(1)
        self.page_creator.create(self.pcb,1)

    def test_pcb_ni_idea(self):
        self.assertEqual(2, len(self.pcb.get_pages()))

    def test_i_increment_my_pc_and_ask_if_has_finished(self):
        self.page_holder.increment()
        self.assertTrue(self.page_holder.has_finished())