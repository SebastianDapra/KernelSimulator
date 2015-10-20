__author__ = 'luciano'


class ToyHardDisk:
    def __init__(self):
        self.programs = []

    def load(self,program):
        self.programs.append(program)

    def get_instructions(self,pcb):
        '''
        tenemos que relacionar el pcb con el programa !!!
        :param pcb:
        :return:
        '''