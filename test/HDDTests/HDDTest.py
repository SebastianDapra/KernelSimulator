__author__ = 'luciano'

import unittest
from process.Program import *
from src.HDD.HDD import *


class TestHDD(unittest.TestCase):

    #Arrange
    def setUp(self):
        self.program1 = Program(range(0,10), "Word")
        self.hdd = HDD(10)

    def test_getting_FS(self):
        fs = self.hdd.generate_file_system()
        self.assertEquals(fs.list_folders(), [], "FS Generated from clean disk have no folders")

    def test_serializing_to_HDD(self):
        fs = self.hdd.generate_file_system()
        fs.add_file("word", self.program1)
        self.hdd.serialize_file_system(fs)
        SUTFs = self.hdd.generate_file_system()
        amount_of_folders = len(SUTFs.list_files())
        self.assertEquals(amount_of_folders, 1, "Should have 1 file")
