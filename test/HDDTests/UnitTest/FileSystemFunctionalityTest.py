__author__ = 'luciano'


import unittest
from src.HDD.FileSystemComponents import *
from src.HDD.HDD import *

class FileSystemFunctionalityTest(unittest.TestCase):

    def setUp(self):
        self.main_folder = Folder(None, "/")
        self.fileSystem = FileSystem(None,self.main_folder)
        self.name_luciano_folder = "luciano"

    def test_adding_folder_to_file_system(self):
        self.fileSystem.add_folder(self.name_luciano_folder)
        luciano_folder =self.fileSystem.get_folder_by_name(self.name_luciano_folder)
        self.assertTrue("luciano" in self.fileSystem.list_folders_names())
        self.assertEquals("luciano",luciano_folder.get_relative_address())
        self.assertEquals("//luciano",luciano_folder.get_absolute_address())

