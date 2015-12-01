import unittest
from src.HDD.HDD import HDD
from src.PCB.PCB import PCB
from src.Memory.MemoryManager import *
from src.Kernel.Program import *
from src.MemoryManagment.ContinuousAssigment.CAPolicies import *
from src.PCB.PCBInfoHolder import BlockHolder
from src.Instruction.Instruction import *


class MemoryManagerTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.hdd = HDD(10)
        self.fs = self.hdd.generate_file_system()
        self.instruction1 = InstructionIO()
        self.instruction2 = InstructionCPU()
        self.instruction3 = InstructionIO()
        self.instructionsForMonkeyIsland = [self.instruction1, self.instruction2]
        self.instructionForManiacManson = [self.instruction1, self.instruction2, self.instruction3]
        self.monkeyIsland = Program("MonkeyIsland",self.instructionsForMonkeyIsland)
        self.maniacManson = Program("ManiacManson",self.instructionForManiacManson)
        self.fs.add_file("MonkeyIsland", self.monkeyIsland)
        self.fs.add_file("ManiacManson", self.maniacManson)
        self.monkeyIslandProgram = self.fs.get_program("MonkeyIsland")
        self.maniacMansonProgram = self.fs.get_program("ManiacManson")
        self.pcb1 = PCB(0, 2, BlockHolder(self.monkeyIslandProgram))
        self.pcb2 = PCB(0, 3 , BlockHolder(self.maniacMansonProgram))
        self.memoryManager = MemoryManager(self.hdd)
        self.memoryManager.set_as_continuous_assignment(FirstFit())

    def test_whenTheMemoryManagerAddsTwoProgramsAndIAskForThe6thPosition_thenIShouldGetException(self):
        self.memoryManager.write(self.pcb1)
        self.memoryManager.write(self.pcb2)
