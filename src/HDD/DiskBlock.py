class DiskBlock:

    def __init__(self, data):
        self._instructions = data

    def __len__(self):
        return len(self._instructions)

    def get_instructions(self):
        return self._instructions


