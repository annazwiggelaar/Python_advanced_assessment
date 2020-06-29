from os import listdir
from os.path import isdir, isfile, join


class FolderDetails():

    def __init__(self, path):
        self.path = path
        if isdir(path):
            # only add files not sub folders
            self.files_to_check = [f for f in listdir(path) if isfile(join(path, f))]
            self.nr_of_files = len(self.files_to_check)

    def get_next_file(self):
        if self.files_to_check:
            # if the list is not empty return the next file from the list
            return self.files_to_check.pop()
        else:
            pass

 #   def check_never_delete(self):
  #      if str(self.files_to_check) not in "Python_advanced_assessment/never_delete":
   #         return self.files_to_check.pop()
    #    else:
     #       pass

