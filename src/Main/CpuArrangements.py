from src.Cpu.InterruptionHandler import *
from src.PCB.PCBInfoHolder import BlockHolder
from test.InterruptionTest.Handler_Loaders import Handle_Loaders
from test.LoaderTest.ToyProgram import *
from src.Kernel.Kernel import *


class CpuArrangements:

    def load_a_instruction_in_a_program(self,a_kernel,scheduler,pcb_table,cpu,memory):
        program = Program("SIN-IO")
        a_kernel.set_scheduler(scheduler)
        a_kernel.set_pcb_table(pcb_table)
        interruption_manager = InterruptionHandler()
        a_kernel.set_interruption_handler(interruption_manager)
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(self, interruption_manager)
        instruction = Instruction("Texto")
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.write_program(program,memory)
        self.setup_load_of_a_program_in_memory(scheduler,pcb_table,cpu,memory,2, program, 1)



    def write_program(self,program,memory):
        pos = 0
        for instruction in program.obtain_instructions():
            memory.put(pos,instruction)

    def load_a_io_instruction_in_a_program(self,a_kernel,scheduler,pcb_table,cpu,memory):
        program = Program("IO")
        a_kernel.set_scheduler(scheduler)
        interruption_manager = InterruptionHandler(cpu)
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(interruption_manager)
        a_kernel.set_interruption_handler(interruption_manager)
        instruction = InstructionIO()
        program.addInstruction(instruction)
        program.addInstruction(instruction)
        self.write_program(program,memory)
        self.setup_load_of_a_program_in_memory(a_kernel,scheduler,pcb_table,cpu,memory,2, program, 2)

    def setup_load_of_a_program_in_memory(self,scheduler,pcb_table,cpu,memory,amount_instructions, program, pcb_id):
        block_holder = BlockHolder(program)
        block_holder.set_representation([0,1])
        pcb = PCB(amount_instructions, pcb_id, block_holder)
        scheduler.policy.add_pcb(pcb)
        memory_admin = ToyMemoryAdmin(memory)
        cpu.set_actual_pcb(pcb)
        pcb_table.add(cpu.get_actual_pcb())
        cpu.set_memory_manager(memory_admin)
