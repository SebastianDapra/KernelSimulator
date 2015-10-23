__author__ = 'luciano'


class Instruction:

    def __init__(self, text):
        self.text = text
        self.output = None

    def __call__(self):
        return self

    def text(self):
        return self.text

    def is_io_instruction(self):
        return False

    def set_output_device(self,output):
        self.output = output

    def run(self,):
        self.output.addInstruction(self.text)

