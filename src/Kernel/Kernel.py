__author__ = 'luciano'

from src.Cpu.Cpu import *
from src.Memory.MemoryManager import *
from src.Kernel.Program import *
from src.Scheduler.LongTermScheduler import *


class Kernel:
    def __init__(self, clock,policy_memory=None):
        self.mode = None
        self.pid = 0
        self.scheduler = None
        self._fileSystem = self._hdd.generate_file_system()
        self._memoryManager = MemoryManager(self)
        self.long_term_scheduler = LongTermScheduler()
        self.cpu = Cpu(self)
        self.waiting_queue = []
        self.pcb_table = None
        self.clock = clock
        self.memory_admin = None
        self.interruption_manager = None
        self.hdd = None

    def set_hdd(self,hdd):
        self.hdd = hdd

    def set_memory_policy(self,policy):
        self._memoryManager.set_policy(policy)

    def get_hdd(self):
        return self.hdd

    def set_interruption_manager(self,interruption_manager):
        self.interruption_manager = interruption_manager

    def set_memory_admin(self, memory_admin):
        self.memory_admin = memory_admin

    def set_memory_manager(self, mem):
        self.cpu.set_memory_manager(mem)

    def set_pcb_table(self, table):
        self.pcb_table = table

    def get_interruption_manager(self):
        return self.interruption_manager

    def memory_admin(self):
        return self.memory_admin
    
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

    def execute_itself(self, program_name, path, priority):
        program = Program(program_name)
        self.create_pcb(program, priority)
        self.scheduler.next

    def run(self,program_name):
        print("Running " + program_name + "...")
        program = self._fileSystem.get_program(program_name)
        instructions = self.obtain_instructions(program)
        pcb = self._creatorPCB.create_pcb(len(instructions), program, self._memoryManager.get_policy().get_info_holder(program))
        self._long_term_scheduler.init_process(pcb)

    def obtain_intructions(self,program):
        return [item for sublist in (map(lambda x: x.get_data(), program.fetch_blocks())) for item in sublist]

    @property
    def timing(self):
        self.clock.tick()

    # Signal should make process execution changed
    def signal_handler(self, signal, pcb):
        self.to_kernel_mode()
        self.mode.manage_interruption_from(signal,pcb)
        self.to_user_mode()

    def create_pcb(self, program, priority):
        # This would probably change with memory implementation
        data_to_create_pcb = (program.size(), self.get_pid, priority)
        pcb = self.interruption_manager.manager_for(NewInterruption).handle_signal(data_to_create_pcb, self.pcb_table)
        self.pid += 1
        self.pcb_table.add(pcb)
        #Agrego en memoria
        self.long_term_scheduler.add_pcb(pcb,self.scheduler)


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


