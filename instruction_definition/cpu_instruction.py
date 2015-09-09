class CPU_instruction(Instruction):
    def __init__(self, value):
        self.value = value
        
    def execute_instruction(self,cpu):
        cpu.execute_instruction(self)