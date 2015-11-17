__author__ = 'luciano'

import threading
from src.Cpu.Interruption import TimeoutInterruption


class Clock(threading.Thread):

    def __init__(self, timeout):
        super(Clock, self).__init__()
        self.timeout = timeout

    def tick(self):
        self.join(self.timeout)
        raise TimeoutInterruption()
        '''
            This is actually NOW not working!
        '''