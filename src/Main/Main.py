__author__ = 'luciano'

from src.Cpu.InterruptionManager import *
from src.Memory.Memory import *
from src.Memory.ToyMemory_Admin import *
from src.PCB.PCBInfoHolder import BlockHolder
from test.LoaderTest.ToyProgram import *
from src.Kernel.Kernel import *
from src.Scheduler.Scheduler import *
from src.Main.Arrangements import *
from src.HDD.HDD import *

class Main:

    def __init__(self):
        self.arrangements = Arrangements()
        self.kernel = Kernel()
        self.hdd = HDD(50)
        self.arrangements.arrange_hdd(self.hdd)
        self.arrangements.arrange_memory(self,self.kernel,self.hdd)
        self.scheduler_policy = RoundRobinPolicy(3)
        self.memory_policy = Paging(self.memory_manager.get_memory(), 2, self.hdd)

        self.arrangements.arrange_kernel(self.kernel,self.scheduler_policy, self.hdd, self.memory_policy)





    def run_example(self):

        self.kernel = Kernel(self.scheduler_policy, self.hdd, self.memory_policy)
        self.kernel.run("Word")
        self.kernel.run("Excel")
        self.kernel.run("Powerpoint")

if __name__ == '__main__':
    Main().run_example()