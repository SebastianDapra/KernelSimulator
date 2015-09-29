__author__ = 'luciano'

from src.Cpu.Interrupt import TimeoutInterruption
from src.Scheduler.Scheduler import *
from src.Cpu.Cpu import *
from src.PCB.PCBTable import *
from src.PCB.PCB import *


class Kernel:
    def __init__(self, memory, file_system, clock):
        # self.file_system = file_system(Disc())
        # self.memory_admin = MemoryAdmin(AsignacionContinua(memory))
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

    def get_program(self, program_name, path):
        return self.file_system.find(path, program_name)

    @property
    def get_ready_queue(self):
        return self.scheduler.ready_queue

    def execute(self, program_name, path, priority):
        program = self.get_program(program_name, path)
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
        if self.memory_admin.has_room_for(program.size()):
            initial_pos = self.memory_admin.next_post_free()
            final_pos = (initial_pos + program.size())
            pcb = PCB(initial_pos, final_pos, 0, self.get_pid, priority)
            self.pid += 1
            self.pcb_table.add(pcb)
            self.scheduler.add_pcb(pcb)
            self.memory_admin.save(pcb, program)

        else:
            print("No hay lugar para esto")
