__author__ = 'luciano'


class ToyMemory:
    def __init__(self):
        self.representation = []
        self.index = 0

    def write(self, pcb):
        self.representation.append(pcb)

    def delete(self,pcb):
        self.representation.remove(pcb)

    def write_at(self,instruction,position):
        self.representation.insert(position,instruction)

    def erase_instruction(self,instruction):
        self.representation.remove(instruction)

    def write_program(self,program):
        for instruction in program.instructions:
            self.write_at(instruction,self.index)
            self.index += 1

    def get_instruction_of_cell(self, position):
        return self.representation[position]

    def getNextFreePosition(self):
        return len(self.representation) + 1
