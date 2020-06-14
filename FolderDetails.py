from os import listdir
from os.path import isdir, isfile, join


class FolderDetails():

    def __init__(self, path):
        self.path = path
        if isdir(path):
            # only add files not sub folders
            self.files_to_check = [f for f in listdir(path) if isfile(join(path, f))]

    def get_next_file(self):
        if self.files_to_check:
            # if the list is not empty return the next file from the list
            file = self.files_to_check.pop()
            if str(file) not in "messy_folder/never delete":            # not working yet
                return file
        else:
            return None
