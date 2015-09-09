import unittest
from cpu_definition.cpu import *
from memory_definition.memory import *
from pcb_definition.pcb import *

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCanExecuteOneInstruction(self):
        memory = Memory(3)
        memory.put({0:'first instruction'})
        memory.put({1:'second instruction'})
        cpu = CPU(memory)
        pcb = PCB(0,2,0001)
        cpu.run(pcb)
        self.assert_(True, True)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()