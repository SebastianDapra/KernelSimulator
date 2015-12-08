from src.Kernel.FunctionsForLists import FunctionsForLists


class FileSystem:

    def __init__(self, drive_container, main_folder):
        self._drive_container = drive_container
        self._current_directory = main_folder

    def go_to_parent(self):
        if self._current_directory.get_parent() is not None:
            self._current_directory = self._current_directory.get_parent()

    def get_folder_by_name(self):
        return FunctionsForLists.findFirst(lambda folder : folder.get_relative_address(),self.list_folders())

    def list_folders(self):
        return self._current_directory.get_folders()

    def list_folders_names(self):
        return list(map(lambda name : name.get_relative_address(),
                        self.list_folders()))

    def add_folder(self, folder_name):
        self._current_directory.new_folder(folder_name)

    def add_file(self, file_name, program):
        self._current_directory.new_file(self._drive_container, file_name, program)

    def obtain_names_of_files_in_current(self):
        return list(map(lambda file : file.get_name(),
                        self.list_files_in_current()))

    def list_files_in_current(self):
        return self._current_directory.get_files()

    def get_current(self):
        return self._current_directory

    def get_program(self, file_name):
        return self._current_directory.get_file(file_name)

