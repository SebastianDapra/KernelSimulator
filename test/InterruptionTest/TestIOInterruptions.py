__author__ = 'luciano'

import unittest
from test.InterruptionTest.Handler_Loaders import *
from src.Kernel.Kernel import *
from src.Instruction.Instruction import *
from src.Memory.ToyMemory import *
from src.Memory.ToyMemory_Admin import *


class TestIOInterruption(unittest.TestCase):
    def setUp(self):
        self.kernel = Kernel(None)
        self.cpu = Cpu(self.kernel)
        self.kernel.scheduler = Scheduler(None)
        self.kernel.scheduler.set_as_fifo()
        self.interruption_manager = InterruptionManager(self.cpu)
        self.kernel.set_interruption_manager(self.interruption_manager)
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(self.interruption_manager)
        self.memory = ToyMemory()
        self.memory_manager = ToyMemoryAdmin(self.memory)
        self.cpu.set_memory_manager(self.memory_manager)

    def two_programs_in_ready_queue(self):
        instruction_io = InstructionIO()
        instruction = Instruction("text")
        self.kernel.create_pcb(self.a_program_with_instruction(instruction_io), 0)
        self.kernel.create_pcb(self.a_program_with_instruction(instruction), 1)

    def a_program_with_instruction(self,instruction_io):
        a_program = Program("P")
        for i in range(0,5):
            a_program.addInstruction(instruction_io)
        return a_program

    def test_when_a_process_is_io_then_goes_to_the_waiting_queue(self):
        self.two_programs_in_ready_queue()
        io_pcb = self.kernel.scheduler.ready_queue[0]
        self.cpu.set_actual_pcb(io_pcb)
        without_io_pcb = self.kernel.scheduler.ready_queue[1]
        self.assertEqual(io_pcb.get_pid,self.cpu.actual_pcb.get_pid)
        self.cpu.complete_instruction_cycle()
        self.assertEqual(ProcessState.waiting,io_pcb.state)
        self.assertEqual(without_io_pcb.get_pid,self.cpu.actual_pcb.get_pid)
        self.assertEqual(ProcessState.running,without_io_pcb)