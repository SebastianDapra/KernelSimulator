__author__ = 'luciano'


class Instruction:

    def __init__(self, text):
        self.text = text

    def __call__(self):
        return self

    def text(self):
        return self.text

    def is_io_instruction(self):
        return False

    def run(self, output):
        output.agregarInstruccion(self.text)

