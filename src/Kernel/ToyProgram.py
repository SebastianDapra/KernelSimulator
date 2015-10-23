__author__ = 'luciano'

from src.Instruction.Instruction import *


class ToyProgram:

    def __init__(self, program):
        self.program = program
        self.load_instructions()

    def load_instructions(self):
        self.program.instructions = map(Instruction("Hooo"),range(1, 10))

