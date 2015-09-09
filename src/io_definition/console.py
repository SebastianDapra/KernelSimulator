__author__ = 'luciano'

class Console:

    def __init__(self):
        self._prints = []

    def save(self, instruction):
        self._prints.append(instruction.text())

    def print_strings(self):
        return self._prints