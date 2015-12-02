from src.Cpu.Cpu import Cpu
from src.Cpu.InterruptionHandler import InterruptionHandler
from src.Instruction.Instruction import Instruction, InstructionIO
from src.Kernel.Kernel import Kernel
from src.Kernel.Program import Program
from src.Memory.Memory import Memory
from src.Memory.MemoryManager import MemoryManager
from src.PCB.PCB import PCB
from src.PCB.PCBInfoHolder import BlockHolder
from src.PCB.PCBTable import PCBTable
from src.Scheduler.Scheduler import Scheduler
from test.InterruptionTest.Handler_Loaders import Handle_Loaders


class Helper:
    def __init__(self):
        self.memory = Memory(50)
        self.cpu = Cpu(None)
        self.scheduler = Scheduler()
        self.scheduler.set_as_fifo()
        self.pcb_table = PCBTable()
        self.memory_manager = MemoryManager()

    def load_a_instruction_in_a_program(self):
        program = Program("SIN-IO")
        a_kernel = Kernel(None)
        a_kernel.set_scheduler(self.scheduler)
        a_kernel.set_pcb_table(self.pcb_table)
        interruption_manager = InterruptionHandler()
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
        interruption_manager = InterruptionHandler()
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
        self.cpu.set_memory_manager(self.memory_manager)