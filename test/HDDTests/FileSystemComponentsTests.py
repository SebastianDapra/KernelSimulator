__author__ = 'luciano'

import unittest
from src.HDD.FileSystemComponents import *
from src.HDD.HDD import *


class FileSystemComponentsTest(unittest.TestCase):

    def setUp(self):
        self._hdd = HDD(10)
        self.folder = Folder(None, "/")

    def test_getting_folder_name(self):
        print(self.folder.get_absolute_address())
        self.assertEqual(self.folder.get_absolute_address(), "/")

    def test_adding_three_siblings(self):
        self.folder.new_folder("luciano")
        self.folder.new_folder("sebastian")
        self.folder.new_folder("ivan")
        self.assertEqual(len(self.folder.get_folders()), 3)


