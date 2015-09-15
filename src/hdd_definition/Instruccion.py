class Instruccion:

    def __init__(self, text):
        self.texto = text

    def text(self):
        return self.texto

    def is_io_instruction(self):
        return False

    def run(self, output):
        output.agregarInstruccion(self.texto)
