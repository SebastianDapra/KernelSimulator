from src.MemoryManagment.Paging.Frame import *
from src.MemoryManagment.Paging.PageCreator import *
from src.MemoryManagment.Paging.FrameManager import *
from src.Kernel.FunctionsForLists import *
from src.PCB.PCBInfoHolder import *


class Paging:

    def __init__(self, memory, instructions_per_frame, hdd):
        self._memory = memory
        self._instructions_per_frame = instructions_per_frame
        self._memory_size = self._memory.size()
        self._frames = []
        self.generate_frames()
        self._frame_manager = FrameManager(self._frames, hdd)
        self._page_creator = PageCreator()


    def get_amount_of_frames(self):
        return len(self._frames)

    def __can_create(self):
        return self._memory_size % self._instructions_per_frame == 0


    def get_frame_for_current_instruction(self,pcb):
        self._frame_manager.get_frames_of_pcb(pcb)

    def generate_frames(self):
        if self.__can_create():
            print("Creating frames...")
            self.__create_frames()

    def __create_frames(self):
        index = 0
        for split in range(0, self._memory_size, self._instructions_per_frame):
            self._frames.append(FrameBuilder.crearFrame(index, split, split + self._instructions_per_frame - 1))
            index += 1

    def assign_to_memory(self, pcb):
        #if not pcb.get_information().is_holding():
        self._page_creator.create(pcb, self._instructions_per_frame)
        policy_result = self._frame_manager.map_page_to_frame(pcb)
        return policy_result

    def can_serve(self,pcb):
        return self.get_amount_of_free_frames() >= self.frames_per_pcb(pcb)

    def frames_per_pcb(self,pcb):
        return pcb.get_amount_of_instructions() / self._page_creator.get_instructions_per_frame()


    def get_amount_of_free_frames(self):
        return len(FunctionsForLists.filterList(lambda f: not f.is_in_use(), self._frames))

    def set_memory_manager(self, memory_manager):
        self._memory_manager = memory_manager

    def get_info_holder(self, program):
        return PageHolder(program)