import unittest
from src.PCB.PCBTable import *
from src.PCB.PCB import *


class TestPCB(unittest.TestCase):

    def setUp(self):
        self.pcb_table = PCBTable()

    '''
    Test involving PCBs
    '''

    def test_when_pcb_is_created_then_it_is_add_to_pcb_table_with_state_new(self):
        pass

    def test_when_execution_finishes_pcb_state_pcb_is_deleted_from_table(self):
        pass
