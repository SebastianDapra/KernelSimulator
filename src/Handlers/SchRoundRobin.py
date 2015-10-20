from src.Cpu.Cpu import *
from src.Handlers.SchStrategy import *


class SchRoundRobin (SchStrategy):

    def __init__(self, sch_strategy):
        self.sch_strategy = sch_strategy

    def push_to_queue(self, sts, pcb):
        self.sch_strategy.push_to_queue(sts, pcb)