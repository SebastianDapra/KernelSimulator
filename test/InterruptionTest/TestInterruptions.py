from src.Cpu.Manager import Manager
from src.Memory.Memory import Memory
from src.Memory.MemoryManager import MemoryManager
from src.PCB.PCB import PCB
from src.PCB.PCBTable import PCBTable
from src.Cpu.Cpu import Cpu
from src.Instruction.Instruction import Instruction, InstructionIO
from src.Kernel.Kernel import Kernel
from src.Kernel.Program import Program
from src.PCB.PCBInfoHolder import BlockHolder
from src.Scheduler.Scheduler import Scheduler
import unittest

from src.Scheduler.SchedulerPolicy import FifoPolicy
from test.InterruptionTest.Handler_Loaders import *


class TestInterruption(unittest.TestCase):
    def setUp(self):
        self.cpu = Cpu(None)
        self.kernel = Kernel(None, self.cpu)
        self.cpu.kernel = self.kernel
        self.pcb_table = self.kernel.pcb_table
        self.memory_manager = self.kernel.memory_manager
        self.fifo = FifoPolicy(self.kernel.scheduler)
        self.program = Program("Pepe")
        self.instruction = Instruction("first instruction")
        self.program.addInstruction(self.instruction)
        self.info_unit = [1,2,3,4]
        self.block_holder = BlockHolder(self.program)
        self.block_holder.set_representation(self.info_unit)
        self.pcb = PCB(1, 4, self.block_holder)
        self.pcb_table.add(self.pcb)
        self.cpu.set_actual_pcb(self.pcb)
        self.manager = Manager(self.kernel.scheduler, self.pcb_table, self.memory_manager)
        self.interruption_handler = InterruptionHandler(self.manager)
        self.kernel.set_interruption_handler(self.interruption_handler)

    def test_when_a_process_is_killed_then_it_is_removed_from_the_pcb_table(self):
        self.cpu.execute_single_instruction(self.program.get_instructions().pop())
        self.assertEquals(self.pcb_table.size(), 0)


