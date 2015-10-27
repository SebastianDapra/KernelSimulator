__author__ = 'luciano'


import unittest
from test.InterruptionTest.Handler_Loaders import *


class TestInterruption(unittest.TestCase):
    def setUp(self):
        self.interruption_manager = InterruptionManager(None)
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(self.interruption_manager)

    def test_when_new_process_is_created_and_handler_loaded_then_is_added_in_memory(self):
        for interruption in [(IOInterruption, IOInterruptionManager), (KillInterruption, KillInterruptionManager),
                             (WaitingInterruption, WaitingInterruptionManager),
                             (EndIOInterruption, EndIOInterruptionManager),
                             (NewInterruption, NewInterruptionManager),
                             (TimeoutInterruption, TimeoutInterruptionManager)]:
            self.assertEqual(interruption[1], self.interruption_manager.manager_for(interruption[0]))