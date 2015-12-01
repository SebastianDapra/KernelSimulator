__author__ = 'luciano'

from src.Main.Arrangements import *
from src.HDD.HDD import *
from src.Scheduler.Scheduler import *

class Main:

    def __init__(self):
        self.arrangements = Arrangements()
        self.kernel = Kernel(None)
        self.hdd = HDD(50)
        self.arrangements.arrange_hdd(self.hdd)
        self.arrangements.arrange_memory(self.kernel,self.hdd)
        self.scheduler = Scheduler(None)
        self.scheduler.set_as_round_robin(3)
        self.arrangements.arrange_kernel(self.kernel,self.scheduler,
                                         self.hdd)


    def run_example(self):
        self.kernel.run("Word",2)
        self.kernel.run("Excel",3)
        self.kernel.run("Powerpoint",1)

if __name__ == '__main__':
    Main().run_example()