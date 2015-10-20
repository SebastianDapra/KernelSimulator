__author__ = 'luciano'

from src.Kernel.Output import *


class Program:

    def __init__(self, name):
        self.name = name
        self.instructions = []
        self.output = Output()

    def addInstruction(self, instruction):
        self.instructions.append(instruction)

    def execute(self):
        for instr in self.instructions:
            pass
            instr.run(self.output)

    def size(self):
        return len(self.instructions)

    def getInstructions(self):
        return self.instructions

    def getElementAt(self, position):
        return self.instructions[position]

    def getInstructionExecutedAt(self, index):
        return self.output.get(index)