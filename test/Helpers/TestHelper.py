from src.Cpu.Cpu import Cpu
from src.Cpu.InterruptionHandler import InterruptionHandler
from src.Cpu.Manager import Manager
from src.HDD.HDD import HDD
from src.Instruction.Instruction import Instruction, InstructionIO
from src.Kernel.Kernel import Kernel
from src.Kernel.Program import Program
from src.Memory.Memory import Memory
from src.Memory.MemoryManager import MemoryManager
from src.PCB.PCB import PCB
from src.PCB.PCBInfoHolder import BlockHolder, PageHolder
from src.PCB.PCBTable import PCBTable
from src.Scheduler.Scheduler import Scheduler
from src.Scheduler.SchedulerPolicy import FifoPolicy


class Helper:
    def __init__(self):
        self.memory = Memory(50)
        self.hdd = HDD(5)
        self.cpu = Cpu(None)
        self.scheduler = Scheduler()
        self.fifo = FifoPolicy(self.scheduler)
        self.pcb_table = PCBTable()
        self.memory_manager = MemoryManager()
        self.a_kernel = Kernel(self.cpu, self.memory_manager)
        self.a_kernel.set_scheduler(self.scheduler)
        self.a_kernel.set_pcb_table(self.pcb_table)
        self.a_kernel.set_hdd(self.hdd)
        self.a_kernel.hdd.generate_file_system()
        self.instruction = Instruction("Texto")
        self.instruction_io = InstructionIO("IO")

    def load_a_instruction_in_a_program(self):
        program = Program("SIN-IO")
        manager = Manager(self.scheduler, self.pcb_table, self.memory_manager)
        interruption_handler = InterruptionHandler(manager)
        self.a_kernel.set_interruption_handler(interruption_handler)
        self.cpu.kernel = self.a_kernel
        program.addInstruction(self.instruction)
        program.addInstruction(self.instruction)
        self.write_program(program,self.memory)
        self.setup_load_of_a_program_in_memory(2, program, 1)

    def load_a_io_instruction_in_a_program(self):
        program = Program("IO")
        manager = Manager(self.scheduler, self.pcb_table, self.memory_manager)
        interruption_handler = InterruptionHandler(manager)
        self.a_kernel.set_interruption_handler(interruption_handler)
        self.cpu.kernel = self.a_kernel
        program.addInstruction(self.instruction_io)
        program.addInstruction(self.instruction_io)
        self.write_program(program,self.memory)
        self.setup_load_of_a_program_in_memory(2, program, 2)

    def write_program(self,program,memory):
        pos = 0
        for instruction in program.get_instructions():
            memory.put(pos,instruction)

    def setup_load_of_a_program_in_memory(self, amount_instructions, program, pcb_id):
        page_holder = PageHolder(program)
        pcb = PCB(amount_instructions, pcb_id, page_holder)
        self.pcb_table.add(pcb)
        self.fifo.add_pcb(pcb)
        self.cpu.set_actual_pcb(pcb)