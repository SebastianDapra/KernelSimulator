__author__ = 'luciano'


class Output:
    def __init__(self):
        self.instructions = []
        self.index = 0

    def addInstruction(self, instruccion):
        self.instructions.append(instruccion)
        self.index += 1

    def get(self, index):
        return self.instructions[index]

    def print_all(self):
        for instr in self.instructions:
            print (instr)

