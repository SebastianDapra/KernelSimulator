__author__ = 'luciano'

import jsonpickle
from jsonpickle.compat import unicode
from src.HDD.FileSystemComponents import *
from src.HDD.FileSystem import FileSystem
from src.HDD.DriveContainer import DriveContainer
from src.Kernel.FunctionsForLists import *

class HDD:

    def __init__(self, amount_sector):
        self._drive_container = DriveContainer(self)
        self._sectors = dict.fromkeys(range(1, amount_sector), [])
        self._representation = jsonpickle.encode(FileSystem(self._drive_container, Folder(None, "/")))
        self._swap_area = []

    def get_drive_container(self):
        return self._drive_container

    def get_blocks(self, token):
        return list(map(lambda x: self._sectors[unicode(token.get_sector())][x - 1], token.get_blocks()))

    def add_block(self, sector, block):
        self._sectors[unicode(sector)].append(block)
        return len(self._sectors[unicode(sector)])

    def sectors_size(self):
        return len(self._sectors.keys())

    def generate_file_system(self):
        return jsonpickle.decode(self._representation)

    def display(self,file_system):
        self.__serialize_file_system(file_system)

    def __serialize_file_system(self, file_system):
        self._representation = jsonpickle.encode(file_system)

    def find_page(self, index):
        page = FunctionsForLists.findFirst(self.__conditions_for_finding_page(index), self._swap_area)
        return page

    def __conditions_for_finding_page(self,index):
        return lambda aIndex: aIndex.get_index() != index

    def add_to_swap(self, page):
        self._swap_area.append(page)