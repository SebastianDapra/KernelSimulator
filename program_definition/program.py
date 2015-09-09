__author__ = 'luciano'

    # Tengo un manejador o alguien que me dice cual es el proximo proceso, los datos que ese proceso
    # necesita tienen que cargarse en memoria
    # (sus instrucciones , etc)
    # Con las instrucciones en memoria, el cpu puede procesarlas
    
    
    # Lo que nos piden es , que  dependiendo del tipo de instruccion, el cpu deja de procesarlo (vease si es IO)


class Program:

    def __init__(self, instructions, name):
        self._instructions = instructions
        self._name = name

    def get_instructions(self):
        return self._instructions

    def name(self):
        return self._name

    def add_instruction(self, instruction):
        self._instructions.append(instruction)

    def amount_of_instructions(self):
        return len(self._instructions)