from src.HDD.HDD import HDD
from src.Instruction.Instruction import Instruction
from src.Kernel.Kernel import Kernel
from src.Kernel.Program import Program
from src.Main.Arrangements import Arrangements
from src.Memory.MemoryManager import MemoryManager
from src.Scheduler.SchedulerPolicy import Scheduler, FifoPolicy


class Main:

    def __init__(self):
        self.arrangements = Arrangements()
        self.scheduler = Scheduler()
        self.fifo = FifoPolicy(self.scheduler)
        self.kernel = Kernel(None, self.arrangements.memory_manager, self.scheduler, self.arrangements.hdd)

        #Faltan arranges para que el init quede más chico.

        '''
        Esto deberia ir a un arrange para cargar programas

        instructions1 = []
        instructions2 = []
        instructions3 = []

        for i in range(0,10):
            instructions1.append(Instruction("instr1"))
        for i in range(0,20):
            instructions2.append(Instruction("instr2"))
        for i in range(0,30):
            instructions3.append(Instruction("instr3"))


        Otro arrange para dado un HDD, cargarle archivos al FS

        self.program1 = Program("Word",instructions1)
        self.program2 = Program("Excel",instructions2)
        self.program3 = Program("Powerpoint",instructions3)
        self.hdd = HDD(50)
        self.file_system = self.hdd.generate_file_system()
        self.file_system.add_file("Word", self.program1)
        self.file_system.add_file("Excel", self.program1)
        self.file_system.add_file("Powerpoint", self.program1)
        self.hdd.display(self.file_system)

        '''

        self.arrangements.hddDependencies.load_programs_in_hdd(self.arrangements.hdd)

        '''
        Otro arrange para el manejador de memoria

        self.memory_manager = MemoryManager(self.hdd)
        self.memory_manager.set_policy_as_paging(2)
        '''
        self.arrangements.arrange_memory()
        '''
        Otro arrange para el scheduler
        '''
        self.arrangements.arrange_kernel(self.kernel, self.scheduler, self.fifo)

    def run_example(self):
        self.kernel.set_long_term_scheduler()
        self.kernel.run("Word")
        self.kernel.run("Excel")
        self.kernel.run("Powerpoint")

if __name__ == '__main__':
    Main().run_example()
