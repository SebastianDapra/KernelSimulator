__author__ = 'luciano'

import unittest
from src.Cpu.Interruption import *
from src.Cpu.InterruptionManager import *


class TestInterruptionManager(unittest.TestCase):

    def setUp(self):
        self.interruption_manager= InterruptionManager(None)

    def load_handlers(self):
        for pack_interruption_handler in [(IOInterruption,IOInterruptionManager),(KillInterruption,KillInterruptionManager),
         (WaitingInterruption,WaitingInterruptionManager),(EndIOInterruption,EndIOInterruptionManager),
         (NewInterruption,NewInterruptionManager),(TimeoutInterruption,TimeoutInterruptionManager)]:
            self.interruption_manager.register(pack_interruption_handler)

    def test_when_added_handlers_this_work_fine(self):
        self.load_handlers()
        for interruption in [(IOInterruption,IOInterruptionManager),(KillInterruption,KillInterruptionManager),
         (WaitingInterruption,WaitingInterruptionManager),(EndIOInterruption,EndIOInterruptionManager),
         (NewInterruption,NewInterruptionManager),(TimeoutInterruption,TimeoutInterruptionManager)]:
            self.assertEqual(interruption[1], self.interruption_manager.manager_for(interruption[0]))


