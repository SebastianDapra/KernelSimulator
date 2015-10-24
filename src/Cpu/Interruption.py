__author__ = 'luciano'

'''
Es candidato a pasar a ser un enum, no???
'''

class Interruption():
    pass

class KillInterruption(Interruption):
    pass

class TimeoutInterruption(Interruption):
    pass

class IOInterruption(Interruption):
    pass

class NewInterruption(Interruption):
    pass

class EndIOInterruption(Interruption):
    pass

class WaitingInterruption(Interruption):
    pass

'''
    TimeoutInterruption = 2
    IOInterruption = 3
    NewInterruption = 4
    EndIOInterruption = 5
    WaitingInterruption = 6
'''
