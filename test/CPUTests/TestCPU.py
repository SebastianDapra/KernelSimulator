__author__ = 'luciano'


import unittest

from src.Instruction.Instruction import *
from src.Memory.ToyMemory import *
from src.Memory.ToyMemory_Admin import *
from src.PCB.PCB import *
from src.Cpu.Cpu import *
from src.Kernel.ToyProgram import *
from src.Kernel.Program import *
from src.Kernel.Output import *


class TestCPU(unittest.TestCase):

    def setUp(self):
        self.memory = ToyMemory()
        self.cpu = Cpu(None)

    def load_a_instruction_in_a_program(self):
        program = Program("SIN-IO")
        instruction = Instruction("Texto")
        program.addInstruction(instruction)
        self.memory.write_program(program)
        self.setup_load_of_a_program_in_memory(1)

    def load_a_io_instruction_in_a_program(self):
        program = Program("IO")
        instruction = InstructionIO()
        program.addInstruction(instruction)
        self.memory.write_program(program)
        self.setup_load_of_a_program_in_memory(1)

    def setup_load_of_a_program_in_memory(self,amount_instructions):
        pcb = PCB(amount_instructions,1,None)
        memory_admin = ToyMemoryAdmin(self.memory)
        self.cpu.set_actual_pcb(pcb)
        self.cpu.set_memory_manager(memory_admin)

    def test_given_pcb_when_cpu_complete_instruction_cycle_then_increments_pc(self):
        '''
        Compare the initial state of PCB's PC with final state
        '''
        self.load_a_instruction_in_a_program()
        self.assertEqual(0,self.cpu.actual_pcb.pc)
        self.cpu.complete_instruction_cycle()
        self.assertEqual(1,self.cpu.actual_pcb.pc)

'''
    def test_given_pcb_when_cpu_complete_instruction_cycle_then_has_IO_Interruption(self):
        self.load_a_io_instruction_in_a_program()
        self.assertEqual(0,self.cpu.actual_pcb.pc)
        self.cpu.complete_instruction_cycle()
        self.assertEqual(1,self.cpu.actual_pcb.pc)
'''