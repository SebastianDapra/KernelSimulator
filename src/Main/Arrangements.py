__author__ = 'luciano'


from src.Main.CpuArrangements import *
from src.Main.HDDArrangements import *
from src.Kernel.Kernel import *
from src.Cpu.Clock import *
from src.PCB.PCBTable import *

class Arrangements:

    def __init__(self):
        self.cpuArrangements = CpuArrangements()
        self.hddDependencies = HDDArrangements()

    def arrange_cpu(self,kernel):
        cpu = Cpu(kernel,kernel.memory_admin)
        clock = Clock(cpu)
        kernel.clock = clock
        self.pcb_table = PCBTable()
        self.cpuArrangements.load_a_instruction_in_a_program(kernel
            ,kernel.scheduler,
            self.pcb_table,
            cpu,
            cpu.memory_manager.get_memory())


    def arrange_kernel(self,kernel,scheduler,hdd):
        kernel.set_scheduler(scheduler)
        self.arrange_cpu(kernel)
        kernel.set_hdd(hdd)
        kernel.genetate_file_system()

    def arrange_memory(self,kernel,hdd):
        memory_manager = MemoryManager(hdd)
        self.memory_policy = Paging(memory_manager.get_memory(),
                                    2, hdd)
        kernel.set_memory_admin(memory_manager)

    def arrange_hdd(self,hdd):
        self.hddDependencies.load_programs_in_hdd(hdd)

