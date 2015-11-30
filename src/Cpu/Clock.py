__author__ = 'luciano'

import threading
from src.Cpu.Interruption import TimeoutInterruption


class Clock(threading.Thread):

    def __init__(self, cpu):
        threading.Thread.__init__(self)
        self.cpu = cpu
    '''
    def tick(self):
        self.join(self.timeout)
        raise TimeoutInterruption()
            This is actually NOW not working!
        '''

    def run(self):
        print("Running thread...")
        self.tick()

    def tick(self):
        self.cpu.run()