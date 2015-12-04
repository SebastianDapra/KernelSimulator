from src.Kernel.Loader import Loader
from src.Main.Arrangements import *
from src.HDD.HDD import *
from src.Memory.Memory import Memory
from src.Memory.MemoryManager import MemoryManager
from src.Scheduler.Scheduler import *
from src.Shell.Shell import Shell


class Main:

    def __init__(self):
        self.arrangements = Arrangements()
        self.memory_manager = MemoryManager()
        self.kernel = Kernel(None)

        self.kernel.set_memory_manager(self.memory_manager)
        self.arrangements.arrange_cpu(self.kernel)
        self.hdd = HDD(50)
        self.arrangements.arrange_hdd(self.hdd)
        memory = Memory(2048)
        loader = Loader(self.kernel)
        self.arrangements.arrange_memory(self.kernel,memory,self.hdd)
        self.scheduler = Scheduler(None)
        self.scheduler.set_as_round_robin(3)
        self.arrangements.arrange_kernel(self.kernel,self.scheduler, self.hdd)

    def run_example(self):
        #self.kernel.run("Word")
        #self.kernel.run("Excel")
        #self.kernel.run("Powerpoint")
        Shell(self.kernel).cmdloop()

if __name__ == '__main__':
    Main().run_example()