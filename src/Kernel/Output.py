__author__ = 'luciano'

import unittest

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


class TestsOutput(unittest.TestCase):

    def setUp(self):
        self.output = Output()

    def test_addAnElement(self):
        self.output.addInstruction("soy una instruccion")
        self.assertEquals("soy una instruccion", self.output.get(0))


suite = unittest.TestLoader().loadTestsFromTestCase(TestsOutput)
unittest.TextTestRunner(verbosity=2).run(suite)