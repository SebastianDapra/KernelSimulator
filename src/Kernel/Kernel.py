__author__ = 'luciano'

from src.Cpu.Interrupt import TimeoutInterruption
from src.Scheduler.Scheduler import *
from src.Cpu.Cpu import *
from src.PCB.PCBTable import *
from src.PCB.PCB import *
from src.Kernel.Program import *
from src.Instruction import Instruction


class Kernel:
    def __init__(self, clock):
        self.mode = None
        self.pid = 0
        self.scheduler = None
        self.cpu = Cpu(self) #esto es raro
        self.pcb_table = PCBTable()
        self.clock = clock
        self.memory_admin = None
        self.interruptionManager = None

    def setInterruptionManager(self,interruptionManager):
        self.interruptionManager = interruptionManager

    def set_memory_admin(self, memory_admin):
        self.memory_admin = memory_admin

    def memory_admin(self):
        return self.memory_admin

    def scheduler(self):
        return self.scheduler

    def toKernelMode(self):
        self.mode = KernelMode()

    def toUserMode(self):
        self.mode = UserMode()

    @property
    def get_pid(self):
        return self.pid

    def set_scheduler_policy(self):
        self.scheduler.set_as_fifo

    @property
    def get_ready_queue(self):
        return self.scheduler.ready_queue

    def execute(self, program_name, path, priority):
        program = Program(program_name)
        self.create_pcb(program, priority)
        self.scheduler.next

    @property
    def timing(self):
        self.clock.tick()

    # La senial deberia hacer que la ejecucion de un proceso cambie
    def handle_signal(self, signal, pcb):
        self.toKernelMode()
        self.mode.handle_signal(pcb,signal,self)
        self.toUserMode()

    def create_pcb(self, program, priority):
        # Esto cambiaria con la implementacion de memoria
        initial_pos = 0
        final_pos = (initial_pos + program.size())
        pcb = PCB(initial_pos, final_pos, 0, self.get_pid, priority)
        self.pid += 1
        self.pcb_table.add(pcb)
        self.scheduler.add_pcb(pcb)


class KernelMode:
    def __init__(self):
        pass

    def handle_signal(pcb,signal,kernel):
        try:
            kernel.interruptionManager.managerFor(signal).context_switching(pcb, kernel.cpu, kernel.pcb_table)
        except Exception as e:
            '''
            La Excepcion debe ser una de TimeOut, no una cualquiera !!!!
            '''
            print("Handle unexpected signal! details: " + e.message)
            kernel.interruptionManager.timeoutInterruptionManager().context_switching(pcb, kernel.cpu, kernel.pcb_table)


class UserMode:
    def __init__(self):
        pass

    def handle_signal(pcb,signal,kernel):
        pass