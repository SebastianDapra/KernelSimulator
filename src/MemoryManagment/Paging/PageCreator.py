from src.MemoryManagment.Paging.Page import *


class PageCreator():

    def __init__(self,instructions_per_frame=1):
        self._index = 0
        self._starting = 0
        self._ending = -1
        self.pages = []
        self.instructions_per_frame = instructions_per_frame

    def create(self, pcb, instructions_per_frame):

        self.instructions_per_frame  = instructions_per_frame
        self.__create_pages(pcb.get_amount_of_instructions(),self.instructions_per_frame)

        self.__set_pages_to_pcb(pcb)

    def get_instructions_per_frame(self):
        return self.instructions_per_frame

    def __set_pages_to_pcb(self,pcb):
        pcb.get_memory_policy_for_pcb().set_pages(self.pages)

    def __create_pages(self,amount_of_instructions,instructions_per_frame):
        if amount_of_instructions <= instructions_per_frame:
            page = Page(self._index,self._starting,self._ending + amount_of_instructions,amount_of_instructions)
            self.pages.append(page)
        else:
            self._ending = self._ending + instructions_per_frame
            page = Page(self._index,self._starting,self._ending,instructions_per_frame)
            self.pages.append(page)
            self._starting = self._ending + 1
            self.__create_pages(amount_of_instructions-instructions_per_frame,instructions_per_frame)
