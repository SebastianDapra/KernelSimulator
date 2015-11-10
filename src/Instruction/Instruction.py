__author__ = 'luciano'


class Instruction:

    def __init__(self, text):
        self.text = text

    def __call__(self):
        return self

    def text(self):
        return self.text

    @property
    def is_io(self):
        return False

    def execute(self):
        pass
        #self.output.addInstruction(self.text)


class InstructionIO:

    def __init__(self):
        self.text = "This is an IO Instruction"

    @property
    def is_io(self):
        return True

    def execute(self):
        pass


class InstructionCPU(Instruction):

    def __init__(self):
        self._text = "This is a CPU Instruction"

    def isIO(self):
        return False

    def execute(self):
        pass
