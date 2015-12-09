import unittest
from src.HDD.HDD import HDD
from src.PCB.PCB import PCB
from src.Memory.MemoryManager import *
from src.Kernel.Program import *
from src.MemoryManagment.ContinuousAssigment.CAPolicies import *
from src.PCB.PCBInfoHolder import BlockHolder, PageHolder
from src.Instruction.Instruction import *


class MemoryManagerTest(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.hdd = HDD(10)
        self.fs = self.hdd.generate_file_system()
        self.instruction1 = InstructionIO("IO")
        self.instruction2 = InstructionProgram("An Instruction")
        self.instruction3 = InstructionIO("IO")
        self.instructionsForMonkeyIsland = [self.instruction1, self.instruction2]
        self.instructionForManiacManson = [self.instruction1, self.instruction2, self.instruction3]
        self.monkeyIsland = Program("MonkeyIsland",self.instructionsForMonkeyIsland)
        self.maniacManson = Program("ManiacManson",self.instructionForManiacManson)
        self.fs.add_file("MonkeyIsland", self.monkeyIsland)
        self.fs.add_file("ManiacManson", self.maniacManson)
        self.monkeyIslandProgram = self.fs.get_program("MonkeyIsland")
        self.maniacMansonProgram = self.fs.get_program("ManiacManson")
        self.pcb1 = PCB(0, 2, PageHolder(self.monkeyIslandProgram))
        self.pcb2 = PCB(1, 3 , PageHolder(self.maniacMansonProgram))
        self.memoryManager = MemoryManager(self.hdd)
        self.memoryManager.set_as_paging(2)

    def test_whenTheMemoryManagerAddsTwoProgramsAndIAskForThe6thPosition_thenIShouldGetException(self):
        self.memoryManager.write(self.pcb1)
        self.memoryManager.write(self.pcb2)
