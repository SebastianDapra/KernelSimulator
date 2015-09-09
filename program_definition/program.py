
class Program(object):
    
    def __init__(self,instructions):
        self.instructions = instructions
        
    # Tengo un manejador o alguien que me dice cual es el proximo proceso, los datos que ese proceso necesita tienen que cargarse en memoria
    # (sus instrucciones , etc)
    # Con las instrucciones en memoria, el cpu puede procesarlas
    
    
    # Lo que nos piden es , que  dependiendo del tipo de instruccion, el cpu deja de procesarlo (vease si es IO)