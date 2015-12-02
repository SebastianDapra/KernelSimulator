from src.IO.IODevice import IODevice
from src.Main.CpuArrangements import *
from src.Main.HDDArrangements import *
from src.Kernel.Kernel import *
from src.Cpu.Clock import *
from src.PCB.PCBTable import *


class Arrangements:

    def __init__(self):

        self.hddDependencies = HDDArrangements()

    def arrange_cpu(self,kernel):
        assert (kernel.memory_manager != None)
        cpu = Cpu(kernel)
        clock = Clock(cpu)
        kernel.clock = clock


    def arrange_managers(self,kernel):
        interruption_manager = InterruptionHandler()
        kernel.set_interruption_manager(interruption_manager)
        load_in_interruption_manager = Handle_Loaders()
        load_in_interruption_manager.load_handlers(self, interruption_manager)

    def arrange_kernel(self,kernel,scheduler,hdd):
        kernel.set_scheduler(scheduler)
        kernel.set_hdd(hdd)
        kernel.genetate_file_system()
        self.arrange_managers(kernel)

    def arrange_memory(self,kernel,memory,hdd):
        memory_policy = Paging(memory,2, hdd)
        kernel.memory_manager.set_policy(memory_policy)
        #memory_manager = MemoryManager(hdd,memory_policy)
        #kernel.set_memory_manager(memory_manager)

    def arrange_hdd(self,hdd):
        self.hddDependencies.load_programs_in_hdd(hdd)

