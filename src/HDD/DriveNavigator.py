class Navigator:

    def __init__(self, hdd, sector, block_numbers):
        self._sector = sector
        self._block_numbers = block_numbers
        self._hdd = hdd

    def get_sector(self):
        return self._sector

    def get_blocks(self):
        return self._block_numbers

    def fetch_blocks(self):
        return self._hdd.get_blocks(self)
