__author__ = 'luciano'

from src.Instruction.Instruction import *
from src.Kernel.Program import *

class HDDArrangements:

    def load_programs_in_hdd(self,hdd):
        self.file_system = hdd.generate_file_system()
        self.program1 = Program("Word")
        self.program2 = Program("Excel")
        self.program3 = Program("Powerpoint")
        self.load_instructions(self.program1,10)
        self.load_instructions(self.program2,50)
        self.load_instructions(self.program3,20)
        self.file_system.add_file("Word", self.program1)
        self.file_system.add_file("Excel", self.program1)
        self.file_system.add_file("Powerpoint", self.program1)
        hdd.display(self.file_system)

    def load_instructions(self,program,quantity_of_needed_instructions):
            for i in range(1, quantity_of_needed_instructions):
                program.instructions.append(Instruction("Hooo"))
                program.instructions.append(Instruction("Booo"))