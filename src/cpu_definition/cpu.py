'''
Created on 01/09/2015

@author: sebastian
'''

from handler_cpu.handler import *

class CPU(object):



    def __init__(self, memory):
        self.memory = memory
        self.handler = Handler()
        
    def fetch_instruction(self, pcb):
        return self.memory.get(pcb.base_dir + pcb.pc)

    def run(self,pcb):
        while(pcb.size >= pcb.pc):
            data = self.fetch_instruction(pcb)
            instruction = self.decode_instruction(data)
            instruction.execute_instruction(self)
            pcb.increment()
            
    def decode_instruction(self, data):
        return data
    
    def execute_instruction(self, instruction):
        print(instruction)
    
    def getHandler(self):
        return self.handler
    
        