__author__ = 'luciano'

import unittest
from src.HDD.HDD import HDD
from src.PCB.PCB import PCB
from src.Memory.MemoryManager import *
from process.Program import *
from src.MemoryManagment.ContinuousAssignment.CAPolicies import *
from process.PCBInfoHolder import BlockHolder

class MemoryManagerTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.hdd = HDD(10)
        self.fs = self.hdd.generate_file_system()
        self.instruction1 = InstructionIO()
        self.instruction2 = InstructionCPU()
        self.instruction3 = InstructionIO()
        self.instructionList1 = [self.instruction1, self.instruction2]
        self.instructionList2 = [self.instruction1, self.instruction2, self.instruction3]
        self.program1 = Program(self.instructionList1, "AProgram")
        self.program2 = Program(self.instructionList2, "BProgram")
        self.fs.add_file("AProgram", self.program1)
        self.fs.add_file("BProgram", self.program2)
        self.file1 = self.fs.get_program("AProgram")
        self.file2 = self.fs.get_program("BProgram")
        self.pcb1 = PCB(0, 2, BlockHolder(self.file1))
        self.pcb2 = PCB(0, 3 , BlockHolder(self.file2))
        self.memoryManager = MemoryManager()
        self.memoryManager.set_as_ca(FirstFit())

    def test_whenTheMemoryManagerAddsTwoProgramsAndIAskForThe6thPosition_thenIShouldGetException(self):
        self.memoryManager.write(self.pcb1)
        self.memoryManager.write(self.pcb2)


suite = unittest.TestLoader().loadTestsFromTestCase(MemoryManagerTest)
unittest.TextTestRunner(verbosity=2).run(suite)