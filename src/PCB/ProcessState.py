__author__ = 'luciano'

from enum import Enum

class ProcessState(Enum):
    new = 1
    ready = 2
    running = 3
    waiting = 4
    terminated = 5
