from src.Kernel.FunctionsForLists import *


class WorstFit:

    def __init__(self):
        self

    def find_block(self, free_blocks, pcb):
        blocks_to_sort = FunctionsForLists.filterList(lambda x: x.size() >= pcb.get_amount_of_instructions(), free_blocks)
        return sorted(blocks_to_sort, key=(lambda x: self.get_key(x)))[-1]

    def get_key(self, block):
        return block.size()


class BestFit:

    def __init__(self):
        self

    def find_block(self, free_blocks, pcb):
        blocks = FunctionsForLists.filterList(lambda x: x.size() >= pcb.get_amount_of_instructions(), free_blocks)
        return sorted(blocks, key=(lambda x: self.get_key(x)))[0]

    def get_key(self, block):
        return block.size()


class FirstFit:

    def __init__(self):
        self

    def find_block(self, free_blocks, pcb):
        result = FunctionsForLists.filterList(lambda x: x.size() >= pcb.get_amount_of_instructions(), free_blocks)
        return result[0]

    '''
    Lo escribi asi para que se vea mejor, y puedan debuggear mas comodos.
    Que pasaria si el filter no encuentra nada? Si esto no es normal, arreglenlo.
    Rompo a proposito aca para que vean este comentario.
    '''