from src.Cpu.Manager import Manager
from src.IO.IODevice import IODevice
from src.Main.CpuArrangements import *
from src.Main.HDDArrangements import *
from src.Kernel.Kernel import *
from src.Cpu.Clock import *
from src.MemoryManagment.Paging.Paging import Paging
from src.PCB.PCBTable import *


class Arrangements:

    def __init__(self):
        self.memory_manager = MemoryManager()
        self.hdd = HDD(50)
        self.hddDependencies = HDDArrangements()

    def arrange_cpu(self,kernel):
        cpu = Cpu(kernel)
        clock = Clock(cpu)
        kernel.clock = clock

    def arrange_handlers(self, kernel, scheduler, pcb_table, memory_manager):
        manager = Manager(scheduler, pcb_table, memory_manager)
        interruption_handler = InterruptionHandler(manager)
        kernel.set_interruption_handler(interruption_handler)

    def arrange_kernel(self,kernel,scheduler,policy):
        kernel.set_scheduler(scheduler)
        kernel.set_scheduler_policy(policy)
        self.arrange_handlers(kernel, scheduler, kernel.pcb_table, kernel.memory_manager)

    def arrange_memory(self):
        self.memory_manager.set_policy_as_paging(2)
        #memory_manager = MemoryManager(hdd,memory_policy)
        #kernel.set_memory_manager(memory_manager)

