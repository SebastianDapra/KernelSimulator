from src.HDD.HDD import HDD
import unittest
from src.Kernel.Program import *
from src.MemoryManagment.Paging.FrameManager import *
from src.MemoryManagment.Paging.Frame import *
from src.MemoryManagment.Paging.PageCreator import *
from src.PCB.PCB import *

class FrameManagerTest(unittest.TestCase):

    # Arrange
    def setUp(self):
        program = Program('Excel')
        pageHolder = PageHolder(program)
        self.frame1 = Frame(0, 9, -1)
        self.frame2 = Frame(1, 9, -1)
        self.frame3 = Frame(2, 9, -1)
        self.frame4 = Frame(3, 9, -1)
        self.frames = [self.frame1, self.frame2, self.frame3, self.frame4]
        self.hdd = HDD(50)
        self.frame_manager = FrameManager(self.frames, self.hdd)
        self.page_creator = PageCreator()
        self.pcb = PCB(0, 30, pageHolder)
        self.page_creator.create(self.pcb, 5)

    def test_whenIAssignAPCBTheFirstTime_ThenFrameManagerUsesTheFirstFrame(self):
        # Pages
        first_frame = self.frame_manager.get_frames()[0]
        self.frame_manager.map_page_to_frame(self.pcb)
        first_pcb_page = self.pcb.get_page_assigned_by_number(0)
        self.assertEquals(first_frame.get_page(), first_pcb_page)

    def test_whenTheFirstPCBPageIsUsedAndPCBIsAssigned_ThenFrameManagerUsesTheSecondFrame(self):
        # Pages
        first_pcb_page = self.pcb.get_page_assigned_by_number(0)
        second_pcb_page =self.pcb.get_page_assigned_by_number(1)

        self.frame_manager.map_page_to_frame(self.pcb)
        first_pcb_page.set_used()

        self.frame_manager.map_page_to_frame(self.pcb)
        second_frame = self.frame_manager.get_frames()[1]
        self.assertEquals(second_frame.get_page(), second_pcb_page)

    def test_whenAllFramesAreUsedAndPCBAssignsOneMorePage_ThenTheYoungestFrameGetsEmpty(self):
        # Pages
        first_pcb_page = self.pcb.get_page_assigned_by_number(0)
        second_pcb_page = self.pcb.get_page_assigned_by_number(1)
        assert (second_pcb_page != None)
        third_pcb_page = self.pcb.get_page_assigned_by_number(2)
        forth_pcb_page = self.pcb.get_page_assigned_by_number(3)
        fifth_pcb_page = self.pcb.get_page_assigned_by_number(4)

        self.frame_manager.map_page_to_frame(self.pcb)
        first_pcb_page.set_used()
        self.frame_manager.map_page_to_frame(self.pcb)
        second_pcb_page.set_used()
        self.frame_manager.map_page_to_frame(self.pcb)
        third_pcb_page.set_used()
        self.frame_manager.map_page_to_frame(self.pcb)
        forth_pcb_page.set_used()

        forth_frame = self.frame_manager.get_frames()[3]

        self.frame_manager.map_page_to_frame(self.pcb)
        self.assertEqual(forth_frame.get_page(), fifth_pcb_page)
