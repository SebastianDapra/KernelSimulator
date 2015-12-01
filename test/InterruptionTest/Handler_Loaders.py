from src.Cpu.Interruption import *
from src.Cpu.InterruptionManager import *

class Handle_Loaders:

    @staticmethod
    def load_handlers(self, interruption_manager):
        for pack_interruption_handler in [(IOInterruption, IOInterruptionManager()),
                                          (KillInterruption, KillInterruptionManager()),
                                          (WaitingInterruption, WaitingInterruptionManager()),
                                          (EndIOInterruption, EndIOInterruptionManager()),
                                          (NewInterruption, NewInterruptionManager()),
                                          (TimeoutInterruption, TimeoutInterruptionManager())]:
            interruption_manager.register(pack_interruption_handler)
