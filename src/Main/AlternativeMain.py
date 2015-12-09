from src.HDD.HDD import HDD
from src.Instruction.Instruction import Instruction
from src.Kernel.Kernel import Kernel
from src.Kernel.Program import Program
from src.Memory.MemoryManager import MemoryManager
from src.Scheduler.SchedulerPolicy import Scheduler


class Alternative_main:

    def __init__(self):
        instructions1 = []
        instructions2 = []
        instructions3 = []

        for i in range(0,10):
            instructions1.append(Instruction("instr1"))
        for i in range(0,20):
            instructions2.append(Instruction("instr2"))
        for i in range(0,30):
            instructions3.append(Instruction("instr3"))

        self.program1 = Program("Word",instructions1)
        self.program2 = Program("Excel",instructions2)
        self.program3 = Program("Powerpoint",instructions3)
        self.hdd = HDD(50)
        self.file_system = self.hdd.generate_file_system()
        self.file_system.add_file("Word", self.program1)
        self.file_system.add_file("Excel", self.program1)
        self.file_system.add_file("Powerpoint", self.program1)
        self.hdd.display(self.file_system)
        self.memory_manager = MemoryManager(self.hdd)


    def run_example(self):
        self.memory_manager.set_as_paging(2)
        self.kernel = Kernel(None,self.memory_manager,self.hdd)
        scheduler = Scheduler()
        #scheduler.set_as_rr(3)
        self.kernel.set_scheduler(Scheduler)
        self.kernel.set_long_term_scheduler()
        self.kernel.alternative_run("Word")
        self.kernel.alternative_run("Excel")
        self.kernel.alternative_run("Powerpoint")

if __name__ == '__main__':
    Alternative_main().run_example()
