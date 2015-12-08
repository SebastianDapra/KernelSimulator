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
        self.file_system = FileSystem(self._drive_container, Folder(None, "/"))
        self._watchable_representation_of_FS = jsonpickle.encode(self.file_system)
        self._swap_area = []

    def set_file_system(self,file_system):
        self.file_system = file_system

    def get_file_system(self):
        return self.file_system

    def get_watchable_representation_of_FS(self):
        return self._watchable_representation_of_FS

    def get_drive_container(self):
        return self._drive_container

    def get_blocks(self, a_navigator):
        return list(map(self.blocks_from_give_navigator(a_navigator), a_navigator.get_blocks()))

    def blocks_from_give_navigator(self,a_navigator):
        return lambda x: self._sectors[unicode(a_navigator.get_sector())][x - 1]

    def add_block(self, sector, block):
        self._sectors[unicode(sector)].append(block)
        return len(self._sectors[unicode(sector)])

    def sectors_size(self):
        return len(self._sectors.keys())

    def generate_file_system(self):
        return jsonpickle.decode(self._watchable_representation_of_FS)

    def display(self,file_system):
        self.__serialize_file_system(file_system)

    def __serialize_file_system(self, file_system):
        self._watchable_representation_of_FS = jsonpickle.encode(file_system)

    def find_page(self, page_index):
        page = FunctionsForLists.findFirst(self.__conditions_for_finding_page(page_index), self._swap_area)
        return page

    def __conditions_for_finding_page(self,index):
        return lambda aIndex: aIndex.get_index() == index

    def add_to_swap(self, page):
        self._swap_area.append(page)