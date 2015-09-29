__author__ = 'luciano'

import unittest

class Output:
    def __init__(self):
        self.instrucciones = []
        self.indice = 0

    def agregarInstruccion(self, instruccion):
        self.instrucciones.append(instruccion)
        self.indice += 1

    def get(self, indice):
        return self.instrucciones[indice]

    def print_all(self):
        for instr in self.instrucciones:
            print (instr)


class TestsOutput(unittest.TestCase):

    def setUp(self):
        self.output = Output()

    def test_agregarUnElemento(self):
        self.output.agregarInstruccion("soy una instruccion")
        self.assertEquals("soy una instruccion", self.output.get(0))


suite = unittest.TestLoader().loadTestsFromTestCase(TestsOutput)
unittest.TextTestRunner(verbosity=2).run(suite)