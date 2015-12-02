import cmd


class Shell(cmd.Cmd):
    def __init__(self, kernel):
        super().__init__()
        self.intro = 'Welcome to the KernelSimulator shell. Type help or ? to list commands.\n'
        self.prompt = '>'
        self.kernel = kernel
        self.hdd = kernel.get_hdd()

    def do_run(self, name):
        for file in self.hdd._representation.list_files():

            if name == file._name:
                self.kernel.run(file._program_asociated.name)
                print("Running "+ file._program_asociated.name)

            else:
                print("Program not found")

    def do_EOF(self, line):
        return True