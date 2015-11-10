__author__ = 'luciano'

class FileSystem:

    def __init__(self, drive_saver, main_folder):
        self._drive_saver = drive_saver
        self._current_directory = main_folder

    def go_to_parent(self):
        if self._current_directory.get_parent() is not None:
            self._current_directory = self._current_directory.get_parent()

    def list_folders(self):
        return self._current_directory.get_folders()

    def add_folder(self, folder_name):
        self._current_directory.new_folder(folder_name)

    def add_file(self, file_name, program):
        self._current_directory.new_file(self._drive_saver, file_name, program)

    def list_files(self):
        return self._current_directory.get_files()

    def get_current(self):
        return self._current_directory

    def get_program(self, file_name):
        return self._current_directory.get_file(file_name)

