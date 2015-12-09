from src.Memory.PolicyResult import *
from src.Kernel.FunctionsForLists import *


class PaginationTable():

    def __init__(self):
        pass

    def put_page(self, page, frames, free_frames):
        frame_to_use = free_frames[0]
            #next(iter(free_frames))
        self.update_frames_life(frame_to_use, frames)
        frame_to_use.set_page(page)
        return PolicyResult(frame_to_use.get_starting_index(), frame_to_use.get_ending_index())

    def update_frames_life(self, frame, frames):
        frames_to_update = FunctionsForLists.filterList(lambda x: x is not frame, frames)
        frame.reset_life()
        for x in frames_to_update:
            x.increase_life()