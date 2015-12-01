class Block:

    def __init__(self, id, startIndex, endIndex):
        self._id = id
        self._startIndex = startIndex
        self._endIndex = endIndex
        self._isFree = True
        self._previousBlock = None
        self._nextBlock = None
        self._size = endIndex - startIndex + 1

    def changeStartIndex(self, newStartIndex):
        self._startIndex = newStartIndex

    def changeEndIndex(self, newEndIndex):
        self._endIndex = newEndIndex

    def isFree(self):
        return self._isFree

    def setUsed(self):
        self._isFree = False

    def setFree(self):
        self._isFree = True

    def increaseId(self):
        self._id += 1

    # Avoids recursion.
    def changePreviousBlock(self, newPreviousBlock):
        self._previousBlock = newPreviousBlock

    def changePreviousBlock_double(self, newPreviousBlock):
        self._previousBlock = newPreviousBlock
        newPreviousBlock.changeNextBlock(self)

    # Avoids recursion.
    def changeNextBlock(self, newNextBlock):
        self._nextBlock = newNextBlock

    def changeNextBlock_double(self, newNextBlock):
        self._nextBlock = newNextBlock
        newNextBlock.changePreviousBlock(self)

    def getNextBlock(self):
        return self._nextBlock

    def getPreviousBlock(self):
        return self._previousBlock

    def size(self):
        return self._size

    def decrease_size(self, size):
        self._size -= size

    def increase_size(self, size):
        self._size += size

    def get_id(self):
        return self._id

    def get_start_index(self):
        return self._startIndex

    def set_id(self, new_id):
        self._id = new_id

    def get_end_index(self):
        return self._endIndex
