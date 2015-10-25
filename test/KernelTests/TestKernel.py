__author__ = 'luciano'

import unittest
from src.Kernel.Kernel import *
from src.Cpu.Interruption import *
from src.Cpu.InterruptionManager import *
from src.PCB.PCB import *


class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.kernel = Kernel(None)
        self.kernel.set_interruption_manager(InterruptionManager(None))
        self.kernel.to_kernel_mode

    def load_handlers(self):
        for interruption in [(IOInterruption,IOInterruptionManager),(KillInterruption,KillInterruptionManager),
         (WaitingInterruption,WaitingInterruptionManager),(EndIOInterruption,EndIOInterruptionManager),
         (NewInterruption,NewInterruptionManager),(TimeoutInterruption,TimeoutInterruptionManager)]:
            self.kernel.add_handlers(interruption)

    def test_when_added_handlers_this_work_fine(self):
        self.load_handlers()
        for interruption in [(IOInterruption,IOInterruptionManager),(KillInterruption,KillInterruptionManager),
         (WaitingInterruption,WaitingInterruptionManager),(EndIOInterruption,EndIOInterruptionManager),
         (NewInterruption,NewInterruptionManager),(TimeoutInterruption,TimeoutInterruptionManager)]:
            self.assertEqual(interruption[1], self.kernel.interruption_manager.manager_for(interruption[0]))


