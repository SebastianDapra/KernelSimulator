from src.HDD.HDD import HDD
from src.Instruction.Instruction import *
from src.Kernel.Program import *


class HDDArrangements:

    def load_programs_in_hdd(self, hdd):
        instructions1 = []
        instructions2 = []
        instructions3 = []

        for i in range(0,10):
            instructions1.append(Instruction("instr1"))
        for i in range(0,20):
            instructions2.append(Instruction("instr2"))
        for i in range(0,30):
            instructions3.append(Instruction("instr3"))

        program1 = Program("Word", instructions1)
        program2 = Program("Excel", instructions2)
        program3 = Program("Powerpoint", instructions3)
        file_system = hdd.generate_file_system()
        file_system.add_file("Word", program1)
        file_system.add_file("Excel", program2)
        file_system.add_file("Powerpoint", program3)
        hdd.display(file_system)
        #hdd.display(self.file_system)

    '''
    def load_instructions(self,program, quantity_of_needed_instructions):
            for i in range(1, quantity_of_needed_instructions):
                program.instructions.append(InstructionProgram("Hooo"))
                program.instructions.append(InstructionProgram("Booo"))
                program.instructions.append(InstructionIO("Teclado"))

    '''