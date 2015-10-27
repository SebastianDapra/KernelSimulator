from src.Cpu.Cpu import Cpu
from src.Instruction.Instruction import Instruction, InstructionIO
from src.Kernel.Kernel import Kernel
from src.Kernel.Program import Program
from src.Memory.ToyMemory import ToyMemory
from src.Memory.ToyMemory_Admin import ToyMemoryAdmin
from src.Scheduler.Scheduler import Scheduler

__author__ = 'luciano'


import unittest
from test.InterruptionTest.Handler_Loaders import *


class TestInterruption(unittest.TestCase):
    def setUp(self):
        self.kernel = Kernel(None)
        self.kernel.scheduler = Scheduler()
        self.kernel.scheduler.set_as_fifo()
        self.cpu = Cpu(self.kernel)
        self.pcb = PCB(1, 4, 1)
        self.cpu.set_actual_pcb(self.pcb)
        self.interruption_manager = InterruptionManager(self.cpu)
        self.kernel.set_interruption_manager(self.interruption_manager)
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(self.interruption_manager)
        #self.new_interruption = NewInterruptionManager()
        self.program = Program("Pepe")
        self.instruction = Instruction("first instruction")
        self.program.addInstruction(self.instruction)

        self.memory = ToyMemory()
        self.memory_manager = ToyMemoryAdmin(self.memory)
        self.cpu.set_memory_manager(self.memory_manager)

    def test_when_new_process_is_created_and_handler_loaded_then_the_pid_is_increased_and_the_pcb_is_added_to_pcb_table(self):
        self.kernel.create_pcb(self.program, 1)
        self.assertEqual(self.kernel.pid, 1)
        self.assertEqual(len(self.kernel.pcb_table.pcbs), 1)

    '''
    def test_when_a_process_is_killed_then_it_is_removed_from_the_pcb_table(self):
        self.cpu.execute_single_instruction(self.program.get_instructions().pop())
        self.assertEqual(len(self.kernel.pcb_table.pcbs), 0)
    '''

    def test_when_a_process_is_io_then_goes_to_the_waiting_queue(self):
        io_pcb = PCB(1, 4, 1)
        instruction_io = InstructionIO()
        a_program = Program("P")
        a_program.addInstruction(instruction_io)
        self.cpu.set_actual_pcb(io_pcb)
        self.cpu.complete_instruction_cycle()
        self.assertEqual(io_pcb.state, ProcessState.waiting)
