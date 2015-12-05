class Instruction: #TODO: VER Y ENTENDER EL PATRON COMMAND

    def __init__(self, text):
        self.text = text

    def __call__(self):
        return self

    def text(self):
        return self.text

    def is_io(self):
        raise NotImplementedError

    def execute(self):
        print(self.text)


class InstructionIO(Instruction):

    def __init__(self, text):
        super().__init__(text)

    def is_io(self):
        return True

    def execute(self):
        super().execute()


class InstructionProgram(Instruction):

    def __init__(self, text):
        super().__init__(text)

    def is_io(self):
        return False

    def execute(self):
        super().execute()
