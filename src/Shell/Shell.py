from src.PCB.PCBCreator import PCBCreator


class Shell:
    def __init__(self, prog_loader, pcb_table):
        self.loader = prog_loader
        self.pcb_table = pcb_table
        self.pcb_creator = PCBCreator()

    def execute_my_program(self, program, m_policy):
        self.loader.load(program)
        self.pcb_creator.create_pcb(program.size(), program, m_policy)