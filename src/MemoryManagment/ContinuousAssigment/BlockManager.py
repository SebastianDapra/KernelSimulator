from src.MemoryManagment.ContinuousAssigment.Block import *

class BlocksManager:

    def __init__(self):
        pass

    def divide_block(self, pcb, block_to_used, blocks):
        if self.pcb_has_same_size_than_block(pcb, block_to_used):
            block_to_used.setUsed()
            pcb.get_information().set_block(block_to_used)
        else:
            new_block = self.create_new_block_from(block_to_used, pcb)
            new_block.setUsed()
            self.update_blocks_references(block_to_used, new_block)
            block_to_used.decrease_size(new_block.size())
            blocks.insert(block_to_used.get_id(), new_block)
            self.update_blocks_ids_from(block_to_used)
            pcb.get_information().set_representation(new_block)

    def pcb_has_same_size_than_block(self, pcb, block_to_use):
        return pcb.get_amount_of_instructions() == block_to_use.size()

    def update_blocks_ids_from(self, block_to_use):
        block_to_use.increaseId()
        next_block = block_to_use.getNextBlock()
        while next_block != None:
            next_block.increaseId()
            next_block = next_block.getNextBlock()

    def create_new_block_from(self, block_to_use, pcb):
        new_block_id = block_to_use.get_id()
        new_block_start_index = block_to_use.get_start_index()
        new_block_end_index = new_block_start_index + pcb.get_amount_of_instructions() - 1
        block_to_use.changeStartIndex(new_block_end_index + 1)
        return Block(new_block_id, new_block_start_index, new_block_end_index)

    def update_blocks_references(self, block_to_use, new_block):
        if (block_to_use.getPreviousBlock() != None):
            new_block.changePreviousBlock_double(block_to_use.getPreviousBlock())
        else:
            new_block.changePreviousBlock(block_to_use.getPreviousBlock())
        new_block.changeNextBlock_double(block_to_use)