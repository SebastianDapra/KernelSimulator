from src.Cpu.Clock import Clock
from src.Kernel.Program import *
from src.Scheduler.LongTermScheduler import *
from src.PCB.PCBCreator import *
from src.PCB.PCBTable import *


class Kernel:
    def __init__(self, cpu, loader=None, memory_manager=None):
        self.mode = None
        self.pid = 0
        self.scheduler = None
        self.loader = loader
        self.memory_manager = memory_manager
        self.interruption_handler = None
        self.hdd = None
        self._fileSystem = None
        self.long_term_scheduler = LongTermScheduler()
        self.cpu = cpu
        self._creatorPCB = PCBCreator()
        self.pcb_table = PCBTable()
        self.clock = Clock(self.cpu) or None

    def set_loader(self,loader):
        self.loader = loader

    def genetate_file_system(self):
        self._fileSystem = self.hdd.generate_file_system()

    def set_hdd(self,hdd):
        self.hdd = hdd
        self.memory_manager._hdd = hdd

    def get_hdd(self):
        return self.hdd

    def set_interruption_handler(self, interruption_manager):
        self.interruption_handler = interruption_manager

    def set_memory_manager(self, memory_admin):
        self.memory_manager = memory_admin

    def set_pcb_table(self, table):
        self.pcb_table = table

    def get_interruption_handler(self):
        return self.interruption_handler

    def memory_manager(self):
        return self.memory_manager
    
    def scheduler(self):
        return self.scheduler

    def set_scheduler(self, scheduler):
        self.scheduler = scheduler

    def set_default_kernel_mode(self):
        self.to_user_mode()

    def to_kernel_mode(self):
        self.mode = KernelMode(self)

    def to_user_mode(self):
        self.mode = UserMode(self)

    @property
    def get_pid(self):
        return self.pid

    @property
    def get_ready_queue(self):
        return self.scheduler.ready_queue

    def generate_page_holder(self):
        return PageHolder()

    def load_process(self,program_name):
        program = Program(program_name)
        self.loader.load(self.memory_manager,program)
    '''
    def execute_itself(self, program_name):
        print("Running " + program_name + "...")
        program = Program(program_name)
        pageHolder = PageHolder()
        self.create_pcb(program,pageHolder)
        self.cpu.run()
    '''

    def run(self,program_name):
        print("Running " + program_name + "...")
        self.load_process(program_name)
        print("Finish running " + program_name)

    # Signal should make process execution changed
    def send_signal(self, signal, pcb):
        self.to_kernel_mode()
        self.mode.manage_interruption_from(signal, pcb)
        self.to_user_mode()


class KernelMode:

    '''
    TODO: Restrictions according to the mode the kernel is in:
    For example: While on kernel mode, no other (concurrent) process can make a progress
    '''

    def __init__(self,kernel):
        self.kernel = kernel

    def manage_interruption_from(self, interruption, pcb):
        #self.manager_for(interruption).handle_signal(pcb,self.kernel.cpu,self.kernel.pcb_table)
        self.kernel.interruption_handler.handle(interruption, pcb)


class UserMode:
    def __init__(self,kernel):
        self.kernel = kernel


