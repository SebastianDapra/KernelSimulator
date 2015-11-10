__author__ = 'luciano'


class Folder:

    def __init__(self, parent, folder_name):
        self._parent = parent
        self._absolute_address = self.set_absolute_address(parent, folder_name)
        self._relative_address = folder_name
        self._files = []
        self._siblings = []

    @staticmethod
    def set_absolute_address(parent, folder_name):
        if parent is not None:
            return parent.get_absolute_address() + "/" + folder_name
        # Root case.
        else:
            return folder_name

    def get_absolute_address(self):
        return self._absolute_address

    def get_relative_address(self):
        return self._relative_address

    def new_file(self, drive_saver, file_name, program):
        new_file = File(drive_saver, file_name, program)
        self._files.append(new_file)

    def new_folder(self, folder_name):
        folder = Folder(self, folder_name)
        self._siblings.append(folder)

    def get_file(self, file_name):
        return filter(lambda f: f.get_name() == file_name, self._files)[0]

    def get_folder(self, folder_name):
        return (filter(lambda f: f.get_relative_address() == folder_name, self._siblings))[0]

    def get_files(self):
        return self._files

    def get_folders(self):
        return self._siblings

    def get_parent(self):
        return self._parent

    def get_folder_name(self):
        return self._relative_address


class File:

    def __init__(self, drive_saver, name, program):
        self._name = name
        self._navigator = drive_saver.save_to_hdd(program.get_instructions())

    def get_name(self):
        return self._name

    def fetch_blocks(self):
        return self._navigator.fetch_blocks()