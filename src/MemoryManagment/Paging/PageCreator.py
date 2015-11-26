__author__ = 'luciano'

from src.MemoryManagment.Paging.Page import *
import math


class PageCreator():

    def __init__(self):
        self._index = 0
        self._starting = 0
        self._ending = 0
        self.pages = []

    def create(self, pcb, instructions_per_frame):
       self.pages = self.create_pages(self,pcb.get_amount_of_instructions(),instructions_per_frame,self.pages)
       pcb.get_information().set_representation(self.pages)

    def create_pages(self,amount_of_instructions,instructions_per_frame,pages):

        if amount_of_instructions <= instructions_per_frame:
            pages.append(Page(self._index,self._starting,self._ending + amount_of_instructions,amount_of_instructions))
            return pages
        else:
            self._ending = self._ending + instructions_per_frame
            pages.append(Page(self._index,self._starting,self._ending + instructions_per_frame,instructions_per_frame))
            self._starting = self._ending + 1
            self.create_pages(self,amount_of_instructions,instructions_per_frame,pages)



    '''
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


    def create(self, pcb, instructions_per_frame):


        if pcb.get_amount_of_instructions() % instructions_per_frame == 0:
            cant_pages = pcb.get_amount_of_instructions() // instructions_per_frame
        else:
            cant_pages = (pcb.get_amount_of_instructions() // instructions_per_frame) + 1
        pages = []
        starting_index = 0
        ending_index =
        for cant in range(cant_pages):
            pages.append(Page(self._index, starting_index , ending_index, amount_of_instructions ))
            self._index += 1
        items = range(0, pcb.get_amount_of_instructions())
        divided_items = []
        for i in range(0, len(items), instructions_per_frame):
            divided_items.append(items[i:i+instructions_per_frame])
        pages = []
        for items in divided_items:
            pages.append(Page(self._index, items[0], items[-1], len(items)))
            self._index += 1
        pcb.get_information().set_representation(pages)


    def create_two(self, pcb, instructions_per_frame):
        pages = []
        pcb_inst = pcb.get_amount_of_instructions()
        size_full_pages = int(math.floor(pcb_inst / instructions_per_frame))
        size_not_full_pages = pcb_inst % instructions_per_frame
        for i in xrange(0, size_full_pages, instructions_per_frame -1):
            pages.append(Page(0, i))
    '''
