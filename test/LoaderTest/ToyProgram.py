__author__ = 'luciano'

from src.Instruction.Instruction import *


class ToyProgram:

    def __init__(self, program):
        self.program = program
        self.load_instructions()

    def load_instructions(self):
        for i in range(1, 5):
            self.program.instructions.append(Instruction("Hooo"))
            self.program.instructions.append(Instruction("Booo"))



