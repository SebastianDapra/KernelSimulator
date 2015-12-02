import unittest
from test.InterruptionTest.Handler_Loaders import *


class TestInterruptionManager(unittest.TestCase):
    def setUp(self):
        self.interruption_manager = InterruptionHandler()
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(self, self.interruption_manager)

    def test_when_added_handlers_this_work_fine(self):
        for interruption in [(IOInterruption, IOInterruptionManager()), (KillInterruption, KillInterruptionManager()),
                             (WaitingInterruption, WaitingInterruptionManager()),
                             (EndIOInterruption, EndIOInterruptionManager()),
                             (NewInterruption, NewInterruptionManager()),
                             (TimeoutInterruption, TimeoutInterruptionManager())]:
            self.assertEqual(interruption[1].__class__, self.interruption_manager.manager_for(interruption[0]).__class__)
