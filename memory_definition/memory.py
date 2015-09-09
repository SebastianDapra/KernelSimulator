class Memory(object):

    def __init__(self):
        self.cells = dict()
        self.initialize_cells(size)
    
    def get(self,integer_index):
        self.cells.get(integer_index,None)
    
    def initialize_cells(self, size):
        for index in range(0,size):
            self.cells.update({index:''})
    
    def put(self,cell_and_data):
        #self.cells.keys.includes(cell)
        self.cells.update(cell_and_data)
        
    
        