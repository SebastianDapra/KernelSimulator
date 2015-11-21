import unittest

from src.IO.IODevice import IODevice
from src.IO.IOManager import IOManager
from src.Instruction.Instruction import InstructionIO


class TestIODevice(unittest.TestCase):

    def setUp(self):
        self.io_manager = IOManager()
        self.io_instruction = InstructionIO()
        self.io_manager.send_to_io_queue(self.io_instruction)
        self.io_device = IODevice(self.io_manager)
        self.io_device.add_instruction_to_process()

    def test_i_send_a_io_instruction_from_the_waiting_io_queue_to_the_io_device_for_processing(self):
        self.assertTrue(self.io_device.instructions_to_process.__contains__(self.io_instruction))

    def test_io_device_process_the_io_instruction(self):
        self.io_device.process_io_instruction(self.io_instruction)
        self.assertFalse(self.io_device.instructions_to_process.__contains__(self.io_instruction))