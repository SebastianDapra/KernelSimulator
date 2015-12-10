from src.Cpu.Clock import Clock
from src.Cpu.Cpu import *
from src.Kernel.Loader import Loader
from src.Memory.MemoryManager import *
from src.Kernel.Program import *
from src.Scheduler.LongTermScheduler import *
from src.PCB.PCBCreator import *
from src.PCB.PCBTable import *
from src.Scheduler.SchedulerPolicy import Scheduler


'''
NOTA: NO ESTOY USANDO EL KERNEL PARA NADA
'''
class Kernel:
    def __init__(self, cpu, clock=Clock, memory_manager=MemoryManager(), hdd=None, scheduler=Scheduler(), pcb_table=PCBTable()):
        self.mode = UserMode(self)
        self.pid = 0
        self.hdd = hdd
        self.scheduler = scheduler
        self.scheduler_policy = None
        self.loader = Loader(self)
        self.interruption_handler = None
        self.memory_manager = memory_manager
        self.fileSystem = self.hdd.generate_file_system()
        self.cpu = cpu
        self.long_term_scheduler = None
        self._creatorPCB = PCBCreator()
        self.waiting_queue = []
        self.pcb_table = pcb_table
        self.clock = clock

    def set_loader(self,loader):
        self.loader = loader

    def set_long_term_scheduler(self):
        self.long_term_scheduler = LongTermScheduler(self.scheduler, self.memory_manager)

    def genetate_file_system(self):
        self.fileSystem = self.hdd.generate_file_system()

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

    def set_scheduler_policy(self, policy):
        self.scheduler_policy = policy

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
    '''
    def load_process(self,program_name):
        # traer programa de disco ...
        program = Program(program_name)
        self.loader.load(self.memory_manager,program,self.hdd)

    def execute_itself(self, program_name):
        print("Running " + program_name + "...")
        program = Program(program_name)
        pageHolder = PageHolder()
        self.create_pcb(program,pageHolder)
        self.cpu.run()

    def run(self,program_name):
        print("Running " + program_name + "...")


        program = self._fileSystem.get_program(program_name)
        instructions = self.obtain_instructions(program)
        pcb = self._creatorPCB.create_pcb(len(instructions), program, self.memory_admin.get_policy().get_info_holder(program))
        self.long_term_scheduler.set_short_term_scheduler(self.scheduler)
        self.long_term_scheduler.add_pcb(pcb)

        self.load_process(program_name)
        #self.execute_itself(program_name)
        print("Finish running " + program_name)
    '''
    def run(self,program_name):
        print("Running " + program_name + "...")
        program_file = self.fileSystem.get_program(program_name)
        instructions = self.obtain_instructions(program_file)
        pcb = self._creatorPCB.create_pcb(len(instructions), self.memory_manager.get_policy().get_info_holder(program_file))
        self.long_term_scheduler.initiate_process(pcb)

    def obtain_instructions(self,program_file):
        return [item for sublist in self.list_of_blocks(program_file)
                        for item in sublist]

    def list_of_blocks(self,program_file):
        return list(map(lambda diskBlock: diskBlock.get_instructions(), program_file.fetch_blocks()))

    # Signal should make process execution changed
    def send_signal(self, signal, pcb):
        self.to_kernel_mode()
        self.mode.manage_interruption_from(signal,pcb)
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


