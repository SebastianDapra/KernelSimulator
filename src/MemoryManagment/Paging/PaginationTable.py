__author__ = 'luciano'

from src.Memory.PolicyResult import *

class PaginationTable():

    def __init__(self):
        pass

    def put_page(self, page, frames, free_frames):
        frame_to_use = next(iter(free_frames))
        self.update_frames_life(frame_to_use, frames)
        frame_to_use.set_page(page)
        return PolicyResult(frame_to_use.get_starting_index(), frame_to_use.get_ending_index())

    def update_frames_life(self, frame, frames):
        frames_to_update = filter(lambda x: x is not frame, frames)
        frame.reset_life()
        for frm in frames_to_update:
            frm.increase_life()