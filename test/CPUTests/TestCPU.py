import unittest

from src.Cpu.InterruptionManager import *
from src.Cpu.Interruption import *
from src.Memory.ToyMemory import *
from src.Memory.ToyMemory_Admin import *
from src.Kernel.ToyProgram import *
from src.Kernel.Kernel import *


class TestCPU(unittest.TestCase):
    def setUp(self):
        self.memory = ToyMemory()
        self.cpu = Cpu(None)

    def load_a_instruction_in_a_program(self):
        program = Program("SIN-IO")
        instruction = Instruction("Texto")
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.memory.write_program(program)
        self.setup_load_of_a_program_in_memory(2)

    def load_a_io_instruction_in_a_program(self):
        program = Program("IO")
        a_kernel = Kernel(None)
        interruption_manager = InterruptionManager(self.cpu)
        interruption_manager.register(IOInterruption, IOInterruptionManager())
        a_kernel.set_interruption_manager(interruption_manager)
        self.cpu.kernel = a_kernel
        instruction = InstructionIO()
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.memory.write_program(program)
        self.setup_load_of_a_program_in_memory(2)

    def setup_load_of_a_program_in_memory(self, amount_instructions):
        pcb = PCB(amount_instructions, 1, 0)
        memory_admin = ToyMemoryAdmin(self.memory)
        self.cpu.set_actual_pcb(pcb)
        self.cpu.set_memory_manager(memory_admin)

    def test_given_pcb_when_cpu_complete_instruction_cycle_then_IO_Manager_captures_interruption(self):
        '''
        Compare the initial state of PCB's PC with final state
        '''
        self.load_a_instruction_in_a_program()
        self.assertEqual(0, self.cpu.actual_pcb.pc)
        self.cpu.complete_instruction_cycle()
        self.assertEqual(1, self.cpu.actual_pcb.pc)

    def test_given_pcb_when_cpu_complete_instruction_cycle_then_has_IO_Interruption(self):
        self.load_a_io_instruction_in_a_program()
        self.assertEqual(0, self.cpu.actual_pcb.pc)
        self.cpu.complete_instruction_cycle()
        self.assertEqual(1, self.cpu.actual_pcb.pc)
