from src.Cpu.Cpu import *
from src.Memory.MemoryManager import *
from src.Kernel.Program import *
from src.Scheduler.LongTermScheduler import *
from src.PCB.PCBCreator import *
from src.PCB.PCBTable import *


class Kernel:
    def __init__(self, clock,loader=None, memory_manager=None):
        self.mode = None
        self.pid = 0
        self.scheduler = None
        self.loader = loader
        self.memory_manager = memory_manager
        self.interruption_manager = None
        self.hdd = None
        self._fileSystem=None
        self.long_term_scheduler = LongTermScheduler()
        self.cpu = Cpu(self)
        self._creatorPCB = PCBCreator()
        self.waiting_queue = []
        self.pcb_table = PCBTable()
        self.clock = clock

    def set_loader(self,loader):
        self.loader = loader

    def genetate_file_system(self):
        self._fileSystem = self.hdd.generate_file_system()

    def set_hdd(self,hdd):
        self.hdd = hdd
        self.memory_manager._hdd = hdd


    def set_memory_policy(self,policy):
        self.memory_manager.set_policy(policy)

    def get_hdd(self):
        return self.hdd

    def set_interruption_manager(self,interruption_manager):
        self.interruption_manager = interruption_manager

    def set_memory_manager(self, memory_admin):
        self.memory_manager = memory_admin

    def set_pcb_table(self, table):
        self.pcb_table = table

    def get_interruption_manager(self):
        return self.interruption_manager

    def memory_manager(self):
        return self.memory_manager
    
    def scheduler(self):
        return self.scheduler

    def set_scheduler(self, scheduler):
        self.scheduler = scheduler

    def set_default_kernel_mode(self):
        self.to_user_mode()
        
    def add_handlers(self,pack):
        self.interruption_manager.register(pack)

    def to_kernel_mode(self):
        self.mode = KernelMode(self)

    def to_user_mode(self):
        self.mode = UserMode(self)

    @property
    def get_pid(self):
        return self.pid

    def set_scheduler_policy(self):
        self.scheduler.set_as_fifo

    @property
    def get_ready_queue(self):
        return self.scheduler.ready_queue

    def generate_page_holder(self):
        return PageHolder()

    def load_process(self,program_name):
        program = Program(program_name)
        self.loader.load(self.memory_manager,program)

    def execute_itself(self, program_name):
        print("Running " + program_name + "...")
        program = Program(program_name)
        pageHolder = PageHolder()
        self.create_pcb(program,pageHolder)
        self.cpu.run()

    def run(self,program_name):
        print("Running " + program_name + "...")

        '''
        program = self._fileSystem.get_program(program_name)
        instructions = self.obtain_instructions(program)
        pcb = self._creatorPCB.create_pcb(len(instructions), program, self.memory_admin.get_policy().get_info_holder(program))
        self.long_term_scheduler.set_short_term_scheduler(self.scheduler)
        self.long_term_scheduler.add_pcb(pcb)
        '''
        self.load_process(program_name)
        #self.execute_itself(program_name)
        print("Finish running " + program_name)

    @property
    def timing(self):
        self.clock.tick()

    # Signal should make process execution changed
    def signal_handler(self, signal, pcb):
        self.to_kernel_mode()
        self.mode.manage_interruption_from(signal,pcb)
        self.to_user_mode()

    def create_pcb(self, program, pageHolder):

        size = program.size()
        idPcb = self.get_pid
        #pcb = self.interruption_manager.manager_for(Interruption()).handle_signal(size,idPcb, self.pcb_table,pageHolder)
        self.pid += 1
        self.memory_manager.write(pcb)
        self.long_term_scheduler.add_pcb(pcb,self.scheduler)
        return pcb


class KernelMode:

    '''
    TODO: Restrictions according to the mode the kernel is in:
    For example: While on kernel mode, no other (concurrent) process can make a progress
    '''

    def __init__(self,kernel):
        self.kernel = kernel

    def manage_interruption_from(self,interruption,pcb):
        self.manager_for(interruption).handle_signal(pcb,self.kernel.cpu,self.kernel.pcb_table)

    def manager_for(self,interruption):
        return self.kernel.interruption_manager.manager_for(interruption)


class UserMode:
    def __init__(self,kernel):
        self.kernel = kernel


