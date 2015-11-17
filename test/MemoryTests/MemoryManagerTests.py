__author__ = 'luciano'

import unittest
from src.HDD.HDD import HDD
from src.PCB.PCB import PCB
from src.Memory.MemoryManager import *
from src.Kernel.Program import *
from src.MemoryManagment.ContinuousAssigment.CAPolicies import *
from src.PCB.PCBInfoHolder import BlockHolder
from src.Instruction.Instruction import *
import jsonpickle

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
        self.program1 = Program("AProgram",self.instructionList1)
        self.program2 = Program("BProgram",self.instructionList2)
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
