__author__ = 'luciano'

from src.MemoryManagment.ContinuousAssigment.BlockManager import *
from src.Memory.PolicyResult import *
from src.PCB.PCBInfoHolder import BlockHolder


class ContinuousAssignment:

    def __init__(self, memory, policy):
        self._memory = memory
        self._memory_last_index = self._memory.get_last_index()
        self._blocks = [Block(0, 0, self._memory_last_index)]
        self._free_blocks = self._blocks
        self._policy = policy
        self._blocks_manager = BlocksManager()

    def assign_to_memory(self, pcb):
            print("Attempting to Assign Block for PCB ID: " + str(pcb._id))
            if self.exists_block_with_space(pcb):
                print("Block for PCB ID: " + str(pcb._id) + " successfuly assigned!")
                block_to_use = self._policy.find_block(self._free_blocks, pcb)
                self._blocks_manager.divide_block(pcb, block_to_use, self._blocks)
                self.update_free_blocks()
                pcb.get_information().set_hold((block_to_use.get_start_index(), block_to_use.get_end_index()))
                return PolicyResult(block_to_use.get_start_index(), block_to_use.get_end_index())
            else:
                print("Compact required!")
                self._memory.compact()
                self.compact()
                self.update_free_blocks()
                self.assign_to_memory(pcb)

    def exists_block_with_space(self, pcb):
        result = False
        for block in self._blocks:
            if block.isFree() & (block.size() >= pcb.get_amount_of_instructions()):
                result = True
        return result

    def compact(self):
        used_blocks = filter(lambda x: not x.isFree(), self._blocks)
        start_index_free_block = sum(map(lambda x: x.size(), used_blocks))
        complete_free_block = Block(0, start_index_free_block, self._memory_last_index)
        used_blocks.append(complete_free_block) # We need to do this in two lines. Otherwise, it fails for some reason.
        self._blocks = used_blocks
        self.update_index()
        self.update_references()
        self.update_ids()

    def update_ids(self):
        result = [block.set_id(block_id) for (block, block_id) in zip(self._blocks, range(0, len(self._blocks)))]

    def update_references(self):
        [sndBlock.changePreviousBlock_double(fstBlock) for (fstBlock, sndBlock) in zip(self._blocks[::1], self._blocks[1::1])]
        [sndBlock.changeNextBlock_double(fstBlock) for (fstBlock, sndBlock) in zip(self._blocks[::-1], self._blocks[-2::-1])]
        self._blocks[0].changePreviousBlock(None)
        self._blocks[-1].changeNextBlock(None)

    def update_index(self):
        next_index = 0
        for block in self._blocks:
            block.changeStartIndex(next_index)
            next_index = next_index + block.size() - 1
            block.changeEndIndex(next_index)
            next_index += 1

    def update_free_blocks(self):
        result = []
        for block in self._blocks:
            if block.isFree():
                result.append(block)
        self._free_blocks = result

    def set_memory_manager(self, memory_manager):
        self._memory_manager = memory_manager

    def get_info_holder(self, program):
        return BlockHolder(program)