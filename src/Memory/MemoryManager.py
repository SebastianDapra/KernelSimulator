from src.Memory.Mmu import *
from src.Memory.Memory import Memory
from src.MemoryManagment.ContinuousAssigment.ContinuousAssignment import ContinuousAssignment
from src.MemoryManagment.Paging.Paging import Paging


class MemoryManager:

    def __init__(self, hdd=None,policy=None,memory=Memory(2048)):
        self._next_index = 0
        self._managing_policy = policy
        self.memory = memory
        self._hdd = hdd

    def write(self, pcb):
        '''
        policy_result = self._managing_policy.assign_to_memory(pcb)
        aux = policy_result.get_start_index()
        instructions = pcb.get_instructions()
        '''

        if self.can_serve(pcb):
            self.get_policy().assign_to_memory(pcb)
            self.get_policy().pages_for_pcb(pcb)

        else:
            #pages = self.generate_pages_for_hdd(pcb)
            pass

    def generate_pages_for_hdd(self,pcb):
        self.get_policy().assign_to_hdd(self._hdd,pcb)

    def get_instruction_of(self,pcb):
        return self.pcb.get_memory_policy_for_pcb().current_mem_dir()

    def read(self, mem_dir):
        return self.get_policy().read(mem_dir)
        #return self._memory.get(mem_dir)

    def can_serve(self,pcb):
        return self.get_policy().can_serve(pcb)
        #return self._memory_free_space >= pcb.get_amount_of_instructions()

    def set_as_continuous_assignment(self, ca_policy):
        self._managing_policy = ContinuousAssignment(self.memory, ca_policy)

    def set_as_paging(self, instructions_per_frame):
        self._managing_policy = Paging(self.memory, instructions_per_frame, self._hdd)

    def get_memory(self):
        return self.memory

    def set_memory(self,memory):
        self.memory = memory

    def get_policy(self):
        return self._managing_policy

    def set_policy(self, policy):
        self._managing_policy = policy