class BlockTable:

    def __init__(self):
        self.dictionary = {}

    def put(self, pid, block):
        self.dictionary[pid] = block

    def get(self, pid):
        return self.dictionary[pid]

    def lookup(self, pid):
        return  pid in self.dictionary