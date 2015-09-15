__author__ = 'luciano'


class ProcessState():

    def __init__(self):
        self.enum('new','ready','running','waiting','terminated')

    def enum(*sequential, **named):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        return type('Enum', (), enums)

