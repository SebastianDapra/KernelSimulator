__author__ = 'luciano'


class PolicyResult():

    def __init__(self, start_index, end_index):
        self._start_index = start_index
        self._end_index = end_index

    def get_start_index(self):
        return self._start_index

    def get_end_index(self):
        return self._end_index

