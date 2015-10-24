__author__ = 'luciano'

from src.Cpu.Cpu import *
from src.PCB.PCBTable import *
from src.PCB.PCB import *
from src.Kernel.Program import *


class Kernel:
    def __init__(self, clock):
        self.mode = None
        self.pid = 0
        self.scheduler = None
        self.cpu = Cpu(self) #esto es raro
        self.pcb_table = PCBTable()
        self.clock = clock
        self.memory_admin = None
        self.interruption_manager = None

    def set_interruption_manager(self,interruption_manager):
        self.interruption_manager = interruption_manager

    def set_memory_admin(self, memory_admin):
        self.memory_admin = memory_admin

    def memory_admin(self):
        return self.memory_admin

    def scheduler(self):
        return self.scheduler

    def set_default_kernel_mode(self):
        self.to_user_mode()

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

    @property
    def timing(self):
        self.clock.tick()

    # Signal should make process execution changed
    def handle_signal(self, signal, pcb):
        self.to_kernel_mode()
        self.mode.handle_signal(pcb,signal,self)
        self.to_user_mode()

    def create_pcb(self, program, priority):
        # This would probably change with memory implementation
        initial_pos = 0
        final_pos = (initial_pos + program.size())
        pcb = PCB(initial_pos, final_pos, 0, self.get_pid, priority)
        self.pid += 1
        self.pcb_table.add(pcb)
        self.scheduler.add_pcb(pcb)


class KernelMode:

    '''
    TODO: Restrictions according to the mode the kernel is in:
    For example: While on kernel mode, no other (concurrent) process can make a progress
    '''

    def __init__(self,kernel):
        self.kernel = kernel

    def handle_signal(pcb,signal):
        self.kernel.interruptionManager.manager_for(signal).handle_signal(pcb,self.kernel.cpu,self.kernel.pcb_table)


class UserMode:
    def __init__(self,kernel):
        self.kernel = kernel