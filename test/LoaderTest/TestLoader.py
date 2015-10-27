__author__ = 'luciano'


import unittest
from src.Kernel.Loader import *
from src.Kernel.Program import *
from src.Memory.LogicalMemory import LogicalMemory
from src.Memory.ToyMemory_Admin import *
from src.Memory.ToyMemory import *


class TestLoader(unittest.TestCase):

    def setUp(self):
        self.memory = ToyMemory()
        self.memory_manager = ToyMemoryAdmin(self.memory)
        self.logical_memory = LogicalMemory(self.memory_manager)
        self.program = Program("unPrograma")
        self.program.addInstruction("")
        self.loader = Loader(None,self.logical_memory)

    def test_when_given_loader_and_pcb_then_it_charges_to_memory(self):
        self.assertTrue(len(self.memory.representation) == 0)
        self.loader.load(self.program)
        self.assertFalse(len(self.memory.representation) == 0)