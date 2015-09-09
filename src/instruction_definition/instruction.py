__author__ = 'luciano'

class Instruction:

    def __init__(self, text):
        self._text = text

    def text(self):
        return self._text

    def execute_instruction(self, console):
        console.save(self)


class InstructionIO(Instruction):

    def __init__(self):
        self._text = "This is an IO Instruction"

    def isIO(self):
        return True


class InstructionCPU(Instruction):

    def __init__(self):
        self._text = "This is a CPU Instruction"

    def isIO(self):
        return False