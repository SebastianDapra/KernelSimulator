class IO_Instruction(Instruction):
    def __init__(self,device):
        # tendria que decir con que periferico me comunico y trabajar esa parte
        pass
    
    def execute_instruction(self,cpu):
        cpu.getHandler().execute_instruction(self)