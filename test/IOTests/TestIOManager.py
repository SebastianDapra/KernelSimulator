import unittest

from src.IO.IOManager import IOManager
from src.Instruction.Instruction import InstructionIO


class TestIOManager(unittest.TestCase):

    def setUp(self):
        self.io_manager = IOManager()
        self.io_instruction = InstructionIO()

    def test_i_send_a_io_instruction_to_the_waiting_io_queue(self):
        self.io_manager.send_to_io_queue(self.io_instruction)
        self.assertTrue(self.io_manager.waiting_io_queue.__contains__(self.io_instruction))