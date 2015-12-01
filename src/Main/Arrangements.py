__author__ = 'luciano'

from src.Memory.MemoryManager import *
from src.Main.CpuArrangements import *
from src.Main.HDDArrangements import *
from src.Kernel.Kernel import *
from src.Scheduler.Scheduler import *
from src.Scheduler.SchedulerPolicy import *


class Arrangements:

    def __init__(self):
        self.cpuArrangements = CpuArrangements()
        self.hddDependencies = HDDArrangements()
        self.memory_manager = MemoryManager(None)

    def arrange_cpu(self,kernel):
        pass

    def arrange_kernel(kernel,scheduler_policy,hdd,memory_policy):
        scheduler = Scheduler(scheduler_policy)
        kernel.set_scheduler(scheduler)
        kernel.set_hdd(hdd)
        kernel.set_memory_policy(memory_policy)

    def arrange_memory(self,kernel,hdd):
        self.memory_manager._hdd = hdd

    def arrange_hdd(self,hdd):
        self.hddDependencies.load_programs_in_hdd(hdd)

