__author__ = 'luciano'

from src.MemoryManagment.Paging.Page import *
import math


class PageCreator():

    def __init__(self):
        self._index = 0

    def create(self, pcb, instructions_per_frame):
        items = range(0, pcb.get_amount_of_instructions())
        divided_items = []
        for i in range(0, len(items), instructions_per_frame):
            divided_items.append(items[i:i+instructions_per_frame])
        pages = []
        for items in divided_items:
            pages.append(Page(self._index, items[0], items[-1], len(items)))
            self._index += 1
        pcb.get_information().set_representation(pages)


'''
    def create_two(self, pcb, instructions_per_frame):
        pages = []
        pcb_inst = pcb.get_amount_of_instructions()
        size_full_pages = int(math.floor(pcb_inst / instructions_per_frame))
        size_not_full_pages = pcb_inst % instructions_per_frame
        for i in xrange(0, size_full_pages, instructions_per_frame -1):
            pages.append(Page(0, i))
'''
