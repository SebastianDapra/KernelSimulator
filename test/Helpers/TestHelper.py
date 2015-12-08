from src.Cpu.Cpu import Cpu
from src.Cpu.InterruptionHandler import InterruptionHandler
from src.Cpu.Manager import Manager
from src.Instruction.Instruction import Instruction, InstructionIO
from src.Kernel.Kernel import Kernel
from src.Kernel.Program import Program
from src.Memory.Memory import Memory
from src.Memory.MemoryManager import MemoryManager
from src.PCB.PCB import PCB
from src.PCB.PCBInfoHolder import BlockHolder, PageHolder
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
        a_kernel = Kernel(self.cpu)
        a_kernel.set_scheduler(self.scheduler)
        a_kernel.set_pcb_table(self.pcb_table)
        manager = Manager(self.scheduler, self.pcb_table, self.memory_manager)
        interruption_handler = InterruptionHandler(manager)
        a_kernel.set_interruption_handler(interruption_handler)
        self.cpu.kernel = a_kernel
        instruction = Instruction("Texto")
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.write_program(program,self.memory)
        self.setup_load_of_a_program_in_memory(2, program, 1)

    def load_a_io_instruction_in_a_program(self):
        program = Program("IO")
        a_kernel = Kernel(self.cpu)
        a_kernel.set_scheduler(self.scheduler)
        a_kernel.set_pcb_table(self.pcb_table)
        manager = Manager(self.scheduler, self.pcb_table, self.memory_manager)
        interruption_handler = InterruptionHandler(manager)
        a_kernel.set_interruption_handler(interruption_handler)
        self.cpu.kernel = a_kernel
        instruction = InstructionIO()
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.write_program(program,self.memory)
        self.setup_load_of_a_program_in_memory(2, program, 2)

    def write_program(self,program,memory):
        pos = 0
        for instruction in program.obtain_instructions():
            memory.put(pos,instruction)

    def setup_load_of_a_program_in_memory(self, amount_instructions, program, pcb_id):
        page_holder = PageHolder()
        page_holder.set_representation([0,1])
        pcb = PCB(amount_instructions, pcb_id, page_holder)
        self.pcb_table.add(pcb)
        self.scheduler.policy.add_pcb(pcb)
        self.cpu.set_actual_pcb(pcb)