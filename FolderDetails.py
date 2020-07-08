from os import listdir
from os.path import isdir, isfile, join


class FolderDetails():

    def __init__(self, path):
        self.path = path
        if isdir(path):
            # only add files not sub folders
            self.files_to_check = [f for f in listdir(path) if isfile(join(path, f))]
            self.nr_of_files = len(self.files_to_check)

    def never_delete_file(self, file_name):
        if file_name:
            never_delete = open(join(self.path, "never_delete"), "a")
            never_delete.write(file_name.path)
            never_delete.write("\n")

    def get_next_file(self):
        never_delete = open(join(self.path, "never_delete"), "r").read().splitlines()
        while self.files_to_check:
            # if the list is not empty return the next file from the list
            next_file = self.files_to_check.pop()
            if next_file not in never_delete:
                return next_file
        else:                           # else part of while, while list is not empty get a next file
            pass                        # message that folder cleaning is completed is located in FileDetails

