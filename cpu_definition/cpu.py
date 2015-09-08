'''
Created on 01/09/2015

@author: sebastian
'''

class CPU(object):



    def __init__(self, memory):
        self.memory = memory
        
    def fetch_instruction(self, pcb):
        return self.memory.get(pcb.base_dir + pcb.pc)

    def run(self,pcb):
        while(pcb.size >= pcb.pc):
            data = self.fetch_instruction(pcb)
            self.compute(data)
            pcb.increment()
            
    def compute(self, data):
        instruction = self.decode_instruction(data)
        self.execute_instruction(instruction)
        
    def decode_instruction(self, data):
        return data
    
    def execute_instruction(self, instruction):
        print(instruction)
    
    
    
        