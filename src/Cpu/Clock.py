import threading

from src.Cpu import Interruption


class Clock(threading.Thread):

    def __init__(self, cpu):
        threading.Thread.__init__(self)
        self.cpu = cpu

    def tick(self):
        self.cpu.run()
        self.join(self.timeout)
        raise Interruption.TIMEOUT #TODO: VER!

    def run(self):
        print("Running thread...")
        self.tick()