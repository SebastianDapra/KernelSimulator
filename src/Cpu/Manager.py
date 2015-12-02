from src.IO.IOManager import IOManager
from src.PCB import ProcessState


class Manager:
    def __init__(self, scheduler, pcb_table, memory_manager):
        self._scheduler = scheduler or None
        self.pcb_table = pcb_table or None
        self.memory_manager = memory_manager or None
        self.io_manager = IOManager()

    def manage(self, pcb, interruption):
        if interruption == interruption.KILL:
            self.context_switching(pcb)
            pcb.state = ProcessState.terminated
            self.remove_from_pcb_table(pcb)
            self.memory_manager.remove_instruction(pcb.get_pc())#TODO: Implementar!

        elif interruption == interruption.NEW:
            self.loader.load(self, self.memory_manager, pcb)
            pcb.state = ProcessState.new

        elif interruption == interruption.TIMEOUT:
            super().context_switching(pcb)
            pcb.state = ProcessState.ready

        elif interruption == interruption.IO:
            pcb.state = ProcessState.waiting
            pcb.increment()
            self.io_manager.send_to_io_queue(self._scheduler.cpu.fetch_single_instruction())

        elif interruption == interruption.WAITING:
            pass #TODO: EN DONDE SE LANZA ESTA INTERRUPCION Y QUE HAY QUE HACER?

        elif interruption == interruption.ENDIO:
            self.io_manager.send_to_ready_queue(pcb)#TODO: ARREGLAR!!
            pcb.state = ProcessState.ready

    def context_switching(self, pcb):
        print("Ejecute"+self.__str__())

        next_pcb = self._scheduler.next_process()
        next_pcb.state = ProcessState.running
        '''
            Y como conoce el CPU al prox PCB a ejecutar?
            La CPU mantiene su PCB actual
        '''
        #cpu.read_burst_instruction(next_pcb)

    def remove_from_pcb_table(self, pcb):
        self.pcb_table.remove(pcb)