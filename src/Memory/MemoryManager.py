from src.MemoryManagment.ContinuousAssigment.ContinuousAssignment import *
from src.MemoryManagment.Paging.Paging import *
from src.Memory.Memory import *


class MemoryManager:

    def __init__(self, hdd=None,policy=None):
        self._next_index = 0
        self._policy = policy
        self._hdd = hdd



    def write(self, pcb):
        policy_result = self._policy.assign_to_memory(pcb)
        aux = policy_result.get_start_index()
        instructions = pcb.get_instructions()

        if self.can_serve(pcb):
            self.get_policy().assign_to_memory(pcb)

        else:
            #deberia cargar en disco
            pass

    def get_instruction_of(self,pcb):
        return self.pcb.get_information().current_mem_dir()

    def read(self, mem_dir):
        return self.get_policy().read(mem_dir)
        #return self._memory.get(mem_dir)

    def can_serve(self,pcb):
        return self.get_policy().can_serve(pcb)
        #return self._memory_free_space >= pcb.get_amount_of_instructions()

    def set_as_continuous_assignment(self, ca_policy):
        self._policy = ContinuousAssignment(self._memory, ca_policy)

    def set_as_paging(self, instructions_per_frame):
        self._policy = Paging(self._memory, instructions_per_frame, self._hdd)

    def get_memory(self):
        return self._memory

    def get_policy(self):
        return self._policy

    def set_policy(self, policy):
        self._policy = policy


