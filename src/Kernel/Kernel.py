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
        self.pid = 0
        self.scheduler = Scheduler()
        self.cpu = Cpu(self)
        self.pcb_table = PCBTable()
        self.clock = clock

    @property
    def scheduler(self):
        return self.scheduler

    @property
    def get_pid(self):
        return self.pid

    def set_scheduler_policy(self):
        self.scheduler.set_as_fifo

    @property
    def get_ready_queue(self):
        return self.scheduler.ready_queue

    def execute(self, program_name, path, priority):
        program = Program('Un programa que va a cambiar cuando introduzca el concepto de HD')
        program.addInstruction(Instruction('5 + 5'))
        self.create_pcb(program, priority)
        self.scheduler.get_pcb

    @property
    def timing(self):
        self.clock.tick()

    # La senial deberia hacer que la ejecucion de un proceso cambie
    def handle_signal(self, signal, pcb):
        try:
            signal.alert_cpu(pcb, self.cpu, self.pcb_table)
        except Exception as e:
            print("Handle unexpected signal! details: " + e.message)
            TimeoutInterruption().alert_cpu(pcb, self.cpu, self.pcb_table)

    def create_pcb(self, program, priority):
        # Esto cambiaria con la implementacion de memoria
        initial_pos = 0
        final_pos = (initial_pos + program.size())
        pcb = PCB(initial_pos, final_pos, 0, self.get_pid, priority)
        self.pid += 1
        self.pcb_table.add(pcb)
        self.scheduler.add_pcb(pcb)


