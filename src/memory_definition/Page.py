class Page:

    def __init__(self, frame):
        self.size = frame.get_size()
        self.instruction = []
        self.frame = frame
        self.associate_frame(frame)

    def associate_frame(self, frame):
        frame.set_is_full()

    def get_frame(self):
        return self.frame

    def get_size(self):
        return self.size

    def add_number_instruction(self, instrution):
        self.instruction = instrution

