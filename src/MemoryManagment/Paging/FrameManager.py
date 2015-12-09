from src.MemoryManagment.Paging.PaginationTable import *
from src.Kernel.FunctionsForLists import *


class FrameManager:

    def __init__(self, frames, hdd):
        self._frames = frames
        self._free_frames = frames
        self._table = PaginationTable()
        self._hdd = hdd

    def update_free_frames(self):
        self._free_frames = list(filter(lambda frame: not frame.is_in_use(), self._frames))

    def map_page_to_frame(self, pcb):
        print("Attempting to Assign Page for PCB ID: " + str(pcb._id))
        pcb_pages = pcb.get_pages()
        page = self.__not_used_page(pcb_pages)
        #self._hdd.add_to_swap(page)

        pages = self._hdd.find_page(page.get_index())
        if pages:
            page = pages[0]
        return self.__update_page_and_frames(page)

    def __update_page_and_frames(self,page):

        policy_result = self.assign(page)
        self.update_free_frames()
        return policy_result

    def get_frames_of_pcb(self,pcb):
        self._frames

    def __not_used_page(self,pcb_pages):
        return FunctionsForLists.findFirst(lambda page: not page.has_been_used(), pcb_pages)

    def free_frame_available(self):
        return len(self._free_frames) > 0

    def empty_youngest_frame(self):
        youngest = min(self._frames, key=lambda x: x.get_life())
        self._hdd.add_to_swap(youngest)
        youngest.set_not_in_use()

    def assign(self, page):
        if self.free_frame_available():
            policy_result = self._table.put_page(page, self._frames, self._free_frames)
            print("Page successfuly assigned!")
            return policy_result
        else:
            self.empty_youngest_frame()
            self.update_free_frames()
            print("A frame became empty!")
            self.assign(page)

    def get_frames(self):
        return self._frames
