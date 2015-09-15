__author__ = 'luciano'

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
            print instr