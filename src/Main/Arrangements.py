__author__ = 'luciano'

from src.Memory.MemoryManager import *
from src.Main.CpuArrangements import *
from src.Main.HDDArrangements import *
from src.Kernel.Kernel import *

class Arrangements:

    def __init__(self):
        self.cpuArrangements = CpuArrangements()
        self.hddDependencies = HDDArrangements()

    def arrange_kernel(kernel,scheduler_policy,hdd,memory_policy):
        pass

    def arrange_memory(self,kernel,hdd):
        self.memory_manager = MemoryManager(hdd)

    def arrange_hdd(self,hdd):
        self.hddDependencies.load_programs_in_hdd(hdd)

