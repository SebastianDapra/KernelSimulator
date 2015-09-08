class PCB(object):

    def __init__(self, base_dir,size, id):
        self.base_dir = base_dir
        self.size = size
        self.process_id = id
        self.pc = 0

    
    def increment(self):
        self.pc+=1
    
    def base_dir(self):
        return self.base_dir
    
    def size(self):
        return self.size
    
    def pc(self):
        return self.pc