import unittest

from src.Cpu.Clock import Clock
from src.Cpu.InterruptionManager import *
from src.Memory.ToyMemory import *
from src.Memory.ToyMemory_Admin import *
from src.PCB.PCBInfoHolder import BlockHolder
from test.LoaderTest.ToyProgram import *
from src.Kernel.Kernel import *
from src.Scheduler.Scheduler import *


class TestCPUWithClock(unittest.TestCase):
    def setUp(self):
        self.memory = ToyMemory()
        self.a_kernel = Kernel(None)
        self.cpu = Cpu(self.a_kernel)
        self.scheduler = Scheduler()
        self.scheduler.set_as_fifo()
        self.clock = Clock(self.cpu)

    def load_a_instruction_in_a_program(self):
        program = Program("SIN-IO")
        self.a_kernel.set_scheduler(self.scheduler)
        interruption_manager = InterruptionManager(self.cpu)
        self.a_kernel.set_interruption_manager(interruption_manager)
        instruction = Instruction("Texto")
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.memory.write_program(program)
        self.setup_load_of_a_program_in_memory(2, program, 1)

    def load_a_io_instruction_in_a_program(self):
        program = Program("IO")
        self.a_kernel.set_scheduler(self.scheduler)
        interruption_manager = InterruptionManager(self.cpu)
        interruption_manager.register((IOInterruption, IOInterruptionManager()))
        self.a_kernel.set_interruption_manager(interruption_manager)
        instruction = InstructionIO()
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.memory.write_program(program)
        self.setup_load_of_a_program_in_memory(2, program, 2)

    def setup_load_of_a_program_in_memory(self, amount_instructions, program, pcb_id):
        block_holder = BlockHolder(program)
        block_holder.set_representation([0,1])
        pcb = PCB(amount_instructions, pcb_id, block_holder)
        self.scheduler.policy.add_pcb(pcb)
        memory_admin = ToyMemoryAdmin(self.memory)
        self.cpu.set_actual_pcb(pcb)
        self.cpu.set_memory_manager(memory_admin)

    def test_the_clock_makes_a_tick_and_the_cpu_fetch_a_single_instruction_to_decode(self):
        self.load_a_instruction_in_a_program()
        self.clock.tick()
        self.assertTrue(self.cpu.get_actual_pcb().get_pc() == 1)