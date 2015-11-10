__author__ = 'luciano'

class Frame:

    def __init__(self, index, starting_index, ending_index):
        self._index = index
        self._starting_index = starting_index
        self._ending_index = ending_index
        self._in_use = False
        self._page = None
        self._life = 0

    def is_in_use(self):
        return self._in_use

    def set_in_use(self):
        self._in_use = True

    def set_not_in_use(self):
        self._in_use = False

    def set_page(self, page):
        self._page = page
        self.set_in_use()
        page.set_frame(self)

    def get_page(self):
        return self._page

    def remove_page(self):
        self._page.remove_frame()
        self.set_not_in_use()
        self._page = None

    def increase_life(self):
        self._life += 1

    def reset_life(self):
        self._life = 0

    def get_life(self):
        return self._life

    def get_starting_index(self):
        return self._starting_index

    def get_ending_index(self):
        return self._ending_index