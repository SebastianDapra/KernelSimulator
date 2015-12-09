from src.Instruction.Instruction import Instruction
from src.Kernel.Program import Program
import unittest
from src.Kernel.Program import *
from src.HDD.HDD import *
from test.LoaderTest.ToyProgram import ToyProgram


class TestHDD(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.program1 = Program("Word")
        self.load_instructions()
        self.hdd = HDD(10)

    def load_instructions(self):
        for i in range(1, 10):
            self.program1.instructions.append(Instruction("Hooo"))
            self.program1.instructions.append(Instruction("Booo"))

    def test_getting_FS(self):
        fs = self.hdd.generate_file_system()
        self.assertEquals(fs.list_folders(), [], "FS Generated from clean disk have no folders")

    def test_serializing_to_HDD(self):
        fs = self.hdd.generate_file_system()
        file_name = "a word file"
        fs.add_file(file_name, self.program1)
        expected = fs.obtain_names_of_files_in_current()
        amount_of_files = 1
        self.assertEquals(amount_of_files,len(expected))
        self.assertEquals(file_name,expected[0])
        amount_of_folders = len(fs.list_files_in_current())
        self.assertEquals(amount_of_folders, 1, "Should have 1 file")



        '''
        TODO: WORKING WITH JSON PICKLE
        '''
