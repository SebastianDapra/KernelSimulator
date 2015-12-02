from src.Scheduler.Scheduler import Scheduler
import unittest
from test.InterruptionTest.Handler_Loaders import *
from src.Kernel.Kernel import *
from src.Instruction.Instruction import *
from src.Memory.ToyMemory import *
from src.Memory.ToyMemory_Admin import *
from src.PCB.PCBInfoHolder import BlockHolder


class TestIOInterruption(unittest.TestCase):
    def setUp(self):
        self.kernel = Kernel(None)
        self.kernel.to_user_mode()
        self.kernel.scheduler = Scheduler(None)
        self.kernel.scheduler.set_as_fifo()
        self.interruption_manager = InterruptionHandler(self.kernel.cpu)
        self.kernel.set_interruption_handler(self.interruption_manager)
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(self, self.interruption_manager)
        self.memory = ToyMemory()
        self.memory_manager = ToyMemoryAdmin(self.memory)
        self.kernel.set_memory_manager(self.memory_manager)

    def two_programs_in_ready_queue(self):
        instruction_io = InstructionIO()
        instruction = Instruction("text")
        hold1 = [1,2,3,4]
        hold2 = [5,6,7,8]
        self.block_holder1 = BlockHolder(self.a_program_with_instruction(instruction_io))
        self.block_holder1.set_representation(hold1)
        self.pcb1 = PCB(1, 1, self.block_holder1)
        self.block_holder2 = BlockHolder(self.a_program_with_instruction(instruction))
        self.block_holder2.set_representation(hold2)
        self.pcb2 = PCB(1, 2, self.block_holder2)
        self.kernel.scheduler.push_to_queue(self.pcb1)
        self.kernel.scheduler.push_to_queue(self.pcb2)

    def a_program_with_instruction(self,instruction_io):
        a_program = Program("P")
        for i in range(0,5):
            a_program.addInstruction(instruction_io)
        self.memory.write_program(a_program)
        return a_program

    def test_when_a_process_is_io_then_goes_to_the_waiting_queue(self):
        self.two_programs_in_ready_queue()
        io_pcb = self.kernel.get_ready_queue._get()
        self.kernel.cpu.set_actual_pcb(io_pcb)
        without_io_pcb = self.kernel.get_ready_queue._get()
        self.assertEqual(io_pcb.get_pid,self.kernel.cpu.actual_pcb.get_pid)
        self.kernel.cpu.complete_instruction_cycle()
        self.assertEqual(ProcessState.ProcessState.waiting, io_pcb.get_state)
        self.kernel.cpu.set_actual_pcb(without_io_pcb)
        self.assertEqual(without_io_pcb.get_pid,self.kernel.cpu.actual_pcb.get_pid)
        without_io_pcb.set_state(ProcessState.ProcessState.running)
        self.assertEqual(ProcessState.ProcessState.running, without_io_pcb.get_state)