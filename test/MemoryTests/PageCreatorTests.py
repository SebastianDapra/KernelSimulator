import unittest
from src.PCB.PCB import *
from src.MemoryManagment.Paging.PageCreator import *
from src.Kernel.Program import *

class PageCreatorTest(unittest.TestCase):

    # Arrange
    def setUp(self):
        self.page_creator = PageCreator()
        self.program = Program("Duke Nukem",20)
        id = 0
        cantidadDeInstrucciones = 20
        self.pcb = PCB(id, cantidadDeInstrucciones,PageHolder(self.program))

    def test_whenICreatePagesForPCB_ThenTheInfoHolderHasThemAsItShould(self):
        self.page_creator.create(self.pcb, 5)
        self.assertEqual(len(self.pcb.get_memory_policy_for_pcb().get_pages()), 4)

    def test_whenICreatePagesForPCB_ThenTheInfoTheyHaveIsCorrect(self):
        self.page_creator.create(self.pcb, 5)

        page1 = self.pcb.get_page_assigned_by_number(0)
        page2 = self.pcb.get_page_assigned_by_number(1)
        page3 = self.pcb.get_page_assigned_by_number(2)
        page4 = self.pcb.get_page_assigned_by_number(3)

        self.assertEqual(page1.get_starting_index(), 0)
        self.assertEqual(page1.get_ending_index(), 4)
        self.assertEqual(page1.get_amount_of_instructions(), 5)

        self.assertEqual(page2.get_starting_index(), 5)
        self.assertEqual(page2.get_ending_index(), 9)
        self.assertEqual(page2.get_amount_of_instructions(), 5)

        self.assertEqual(page3.get_starting_index(), 10)
        self.assertEqual(page3.get_ending_index(), 14)
        self.assertEqual(page3.get_amount_of_instructions(), 5)

        self.assertEqual(page4.get_starting_index(), 15)
        self.assertEqual(page4.get_ending_index(), 19)
        self.assertEqual(page4.get_amount_of_instructions(), 5)
