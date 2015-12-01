import unittest

from src.Cpu.InterruptionManager import *
from src.Memory.Memory import *
from src.Memory.ToyMemory_Admin import *
from src.PCB.PCBInfoHolder import BlockHolder
from test.LoaderTest.ToyProgram import *
from src.Kernel.Kernel import *
from src.Scheduler.Scheduler import *
from test.InterruptionTest.Handler_Loaders import Handle_Loaders


class TestCPU(unittest.TestCase):
    def setUp(self):
        self.memory = Memory(50)
        self.cpu = Cpu(None)
        self.scheduler = Scheduler()
        self.scheduler.set_as_fifo()
        self.pcb_table = PCBTable()
        self.memory_admin = ToyMemoryAdmin(self.memory)

    def load_a_instruction_in_a_program(self):
        program = Program("SIN-IO")
        a_kernel = Kernel(None)
        a_kernel.set_scheduler(self.scheduler)
        a_kernel.set_pcb_table(self.pcb_table)
        interruption_manager = InterruptionManager()
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(self, interruption_manager)
        a_kernel.set_interruption_manager(interruption_manager)
        self.cpu.kernel = a_kernel
        instruction = Instruction("Texto")
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.write_program(program,self.memory)
        self.setup_load_of_a_program_in_memory(2, program, 1)

    def load_a_io_instruction_in_a_program(self):
        program = Program("IO")
        a_kernel = Kernel(None)
        a_kernel.set_scheduler(self.scheduler)
        a_kernel.set_pcb_table(self.pcb_table)
        interruption_manager = InterruptionManager()
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(self, interruption_manager)
        a_kernel.set_interruption_manager(interruption_manager)
        self.cpu.kernel = a_kernel
        instruction = InstructionIO()
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.write_program(program,self.memory)
        self.setup_load_of_a_program_in_memory(2, program, 2)

    def write_program(self,program,memory):
        pos = 0
        for instruction in program.get_instructions():
            memory.put(pos,instruction)

    def setup_load_of_a_program_in_memory(self, amount_instructions, program, pcb_id):
        block_holder = BlockHolder(program)
        block_holder.set_representation([0,1])
        pcb = PCB(amount_instructions, pcb_id, block_holder)
        self.pcb_table.add(pcb)
        self.scheduler.policy.add_pcb(pcb)
        self.cpu.set_actual_pcb(pcb)
        self.cpu.set_memory_manager(self.memory_admin)

    def test_given_pcb_when_cpu_complete_instruction_cycle_then_the_Manager_captures_interruption(self):
        '''
        Compare the initial state of PCB's PC with final state
        '''
        self.load_a_instruction_in_a_program()
        self.assertEqual(0, self.cpu.actual_pcb.get_pc())
        self.cpu.complete_instruction_cycle()
        self.assertEqual(1, self.cpu.actual_pcb.get_pc())

    def test_given_pcb_when_cpu_complete_instruction_cycle_then_has_IO_Interruption(self):
        self.load_a_io_instruction_in_a_program()
        self.assertEqual(0, self.cpu.actual_pcb.get_pc())
        self.cpu.complete_instruction_cycle()
        self.assertEqual(1, self.cpu.actual_pcb.get_pc())
