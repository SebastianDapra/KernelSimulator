from threading import Thread

from src.Cpu.Clock import Clock
from src.Cpu.Cpu import Cpu
from src.Cpu.InterruptionManager import InterruptionManager
from src.Kernel.Kernel import Kernel
from src.Kernel.Program import Program
from src.Memory.Memory import Memory
from src.Memory.ToyMemory_Admin import ToyMemoryAdmin
from src.PCB.PCB import PCB
from src.PCB.PCBInfoHolder import BlockHolder
from src.PCB.PCBTable import PCBTable
from src.Scheduler.Scheduler import Scheduler
from test.InterruptionTest.Handler_Loaders import Handle_Loaders
from src.Instruction.Instruction import Instruction, InstructionIO


class Main(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.memory = Memory(50)
        self.a_kernel = Kernel(None)
        self.cpu = Cpu(self.a_kernel)
        self.scheduler = Scheduler()
        self.scheduler.set_as_fifo()
        self.clock = Clock(self.cpu)
        self.a_kernel.clock = self.clock
        self.pcb_table = PCBTable()

    def load_a_instruction_in_a_program(self):
        program = Program("SIN-IO")
        self.a_kernel.set_scheduler(self.scheduler)
        self.a_kernel.set_pcb_table(self.pcb_table)
        interruption_manager = InterruptionManager(self.cpu)
        self.a_kernel.set_interruption_manager(interruption_manager)
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(interruption_manager)
        instruction = Instruction("Texto")
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.write_program(program,self.memory)
        self.setup_load_of_a_program_in_memory(2, program, 1)

    def write_program(self,program,memory):
        pos = 0
        for instruction in program.get_instructions():
            memory.put(pos,instruction)


    def load_a_io_instruction_in_a_program(self):
        program = Program("IO")
        self.a_kernel.set_scheduler(self.scheduler)
        interruption_manager = InterruptionManager(self.cpu)
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(interruption_manager)
        self.a_kernel.set_interruption_manager(interruption_manager)
        instruction = InstructionIO()
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.write_program(program,self.memory)
        self.setup_load_of_a_program_in_memory(2, program, 2)

    def setup_load_of_a_program_in_memory(self, amount_instructions, program, pcb_id):
        block_holder = BlockHolder(program)
        block_holder.set_representation([0,1])
        pcb = PCB(amount_instructions, pcb_id, block_holder)
        self.scheduler.policy.add_pcb(pcb)
        memory_admin = ToyMemoryAdmin(self.memory)
        self.cpu.set_actual_pcb(pcb)
        self.pcb_table.add(self.cpu.get_actual_pcb())
        self.cpu.set_memory_manager(memory_admin)

    def run(self):
        self.load_a_instruction_in_a_program()
        self.cpu.start()

def main():
    main = Main()
    main.start()


if __name__ == "__main__":
    main()