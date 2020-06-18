from tkinter import *
from os import remove, listdir
from os.path import exists, getsize, isdir, isfile, join

from FileDetails import FileDetails
from FolderDetails import FolderDetails


class CleanUpGui(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.master.title("Clean up")
        self.pack(fill=BOTH, expand=1)

        # Setup variables
        self.folder_details = None
        self.current_file = None
        self.del_count = 0
        self.del_bytes_count = 0

        # Setup GUI elements
        self.current_file_name = Label(self)
        self.current_file_size = Label(self)
        self.current_file_preview = Label(self)
        self.current_file_pic_preview = Label(self)
        self.deleted_count = Label(self)
        self.deleted_bytes_count = Label(self)

        self.delete_file_button = Button(self, text="delete", command=self.delete_current_file)
        self.skip_file_button = Button(self, text="skip", command=self.load_next_file)
        self.never_delete_button = Button(self, text="never delete this file", command=self.never_delete_file)

        # Place GUI elements on Canvas
        self.current_file_name.pack()
        self.current_file_size.pack()
        self.current_file_preview.pack()
        self.current_file_pic_preview.pack()
        self.deleted_count.pack()
        self.deleted_bytes_count.pack()

        self.delete_file_button.pack()
        self.skip_file_button.pack()
        self.never_delete_button.pack()

        # create menu
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Choose folder", command=self.change_folder)
        menu.add_cascade(label="File", menu=file)

    # process buttons
    def delete_current_file(self):
        # check if a current file is available
        if self.current_file:
            # delete the current file
            s = getsize(join(self.folder_details.path, self.current_file.path))
            remove(join(self.folder_details.path, self.current_file.path))
            self.del_count += 1
            self.del_bytes_count += s
        # load the next file
        self.load_next_file()

    def never_delete_file(self):
        if self.current_file:
            never_delete = open("never_delete", "a")
            never_delete.write(self.current_file.path)
            never_delete.write("\n")
        self.load_next_file()

    def load_next_file(self):
        if self.folder_details:
            next_file = self.folder_details.get_next_file()
            if next_file:
                self.current_file = FileDetails(self, self.folder_details, next_file)
            else:
                self.current_file = FileDetails(self, self.folder_details, "")
            self.current_file.display_details()

    def change_folder(self):                            # not working
        cleanup = CleanUpGui(self)
        folder_name = input("Which folder would you like to clean?")
        cleanup.select_folder(folder_name)

    # startup
    def select_folder(self, folder_path):
        self.folder_details = FolderDetails(folder_path)
        self.load_next_file()
