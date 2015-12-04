from src.Memory.Memory import Memory
from src.Memory.MemoryManager import MemoryManager
from src.PCB.PCBTable import PCBTable
from src.Cpu.Cpu import Cpu
from src.Instruction.Instruction import Instruction, InstructionIO
from src.Kernel.Kernel import Kernel
from src.Kernel.Program import Program
from src.PCB.PCBInfoHolder import BlockHolder
from src.Scheduler.Scheduler import Scheduler
import unittest
from test.InterruptionTest.Handler_Loaders import *


class TestInterruption(unittest.TestCase):
    def setUp(self):
        self.pcb_table = PCBTable()
        self.kernel = Kernel(None)
        self.kernel.scheduler = Scheduler()
        self.kernel.scheduler.set_as_fifo()
        self.kernel.set_pcb_table(self.pcb_table)
        self.cpu = Cpu(self.kernel)
        self.program = Program("Pepe")
        self.instruction = Instruction("first instruction")
        self.program.addInstruction(self.instruction)
        hold = [1,2,3,4]
        self.block_holder = BlockHolder(self.program)
        self.block_holder.set_representation(hold)
        self.pcb = PCB(1, 4, self.block_holder)
        self.cpu.set_actual_pcb(self.pcb)
        self.interruption_handler = InterruptionHandler()
        self.kernel.set_interruption_handler(self.interruption_handler)
        #self.new_interruption = NewInterruptionManager()

        self.memory = Memory(50)
        self.memory_manager = MemoryManager()
        self.cpu.set_memory_manager(self.memory_manager)

    def test_when_new_process_is_created_and_handler_loaded_then_the_pid_is_increased_and_the_pcb_is_added_to_pcb_table(self):
        self.assertEqual(self.kernel.pid, 1)
        self.assertEqual(len(self.kernel.pcb_table.pcbs), 1)

    def test_when_a_process_is_killed_then_it_is_removed_from_the_pcb_table(self):
        self.kernel.pcb_table.add(self.pcb)
        self.cpu.execute_single_instruction(self.program.get_instructions().pop())
        self.assertEqual(len(self.kernel.pcb_table.pcbs), 0)


