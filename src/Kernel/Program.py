from src.Kernel.Output import *


class Program:

    def __init__(self, name, instructions=[]):
        self.name = name
        self.instructions = instructions
        self.output = Output()

    def addInstruction(self, instruction):
        self.instructions.append(instruction)

    def size(self):
        return len(self.instructions)

    def getElementAt(self, position):
        return self.instructions[position]

    def getInstructionExecutedAt(self, index):
        return self.output.get(index)

    def get_instructions(self):
        return self.instructions

    def name(self):
        return self.name

