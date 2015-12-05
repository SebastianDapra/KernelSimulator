import cmd


class Shell(cmd.Cmd):
    def __init__(self, kernel):
        super().__init__()
        self.intro = 'Welcome to the KernelSimulator shell. Type help or ? to list commands.\n'
        self.prompt = '>'
        self.kernel = kernel
        self.hdd = kernel.get_hdd()

    def do_run(self, name):
        for file in self.hdd.generate_file_system().list_files():

            if name == file._name:
                self.kernel.run(name)
                return print("Running "+ name)

            else:
                return print("Program not found")

    def do_EOF(self, line):
        return self.do_exit(line)

    def do_exit(self, args):
        """Exits from the console"""
        return -1