__author__ = 'luciano'

# Faltaria crear el manejador de memoria, se que nos adelantariamos pero ...
# Ah cambie la representacion de memoria, si bien la de Juli es más cheta esta es más facil para preguntarle un par de cosas

class Memory(object):
    def __init__(self):
        self.records = []
        self.next_position = 0
        self.size = 512
        self.free_cells = 512

    def read(self, position):
        if position > self.size:
            return None
        return self.records[position]

    def write(self, position, instruction):
        self.records.insert(position, instruction)
        self.next_position += 1
        self.free_cells -= 1

    def next_position(self):
        return self.next_position

    def free_memory_to_save(self, program_size):
        return self.free_cells >= program_size

    def size(self):
        return self.size

    def delete(self, index):
        self.records.remove(index)
        self.free_cells += 1
        self.next_position -= 1

    def delete_index(self, index):
        del self.records[index]
        self.free_cells += 1

    def free_cells(self):
        return self.free_cells.numerator
