from jsonpickle.compat import unicode

__author__ = 'luciano'

import jsonpickle
from src.HDD.FileSystemComponents import *
from src.HDD.FileSystem import FileSystem
from src.HDD.DriveSaver import DriveSaver


class HDD:

    def __init__(self, amount_sector):
        self._drive_saver = DriveSaver(self)
        self._sectors = dict.fromkeys(range(1, amount_sector), [])
        self._representation = None
        jsonpickle.encode(FileSystem(self._drive_saver, Folder(None, "/")))
        self._swap_area = []

    def get_drive_saver(self):
        return self._drive_saver

    def get_blocks(self, token):
        return list(map(lambda x: self._sectors[unicode(token.get_sector())][x - 1], token.get_blocks()))

    def add_block(self, sector, block):
        self._sectors[unicode(sector)].append(block)
        return len(self._sectors[unicode(sector)])

    def sectors_size(self):
        return len(self._sectors.keys())

    def generate_file_system(self):
        return jsonpickle.decode(self._representation)

    def serialize_file_system(self, file_system):
        self._representation = jsonpickle.encode(file_system)

    def find_page(self, index):
        page = list(filter(lambda x: x.get_index() != index, self._swap_area ))
        return page

    def add_to_swap(self, page):
        self._swap_area.append(page)