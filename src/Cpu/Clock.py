__author__ = 'luciano'

import threading
from src.Cpu.Interruption import TimeoutInterruption


class Clock:

    def __init__(self, cpu):
        self.cpu = cpu
    '''
    def tick(self):
        self.join(self.timeout)
        raise TimeoutInterruption()
            This is actually NOW not working!
        '''
    def tick(self):
        self.cpu.run()