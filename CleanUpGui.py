from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from os import remove, rename
from os.path import getsize, join, splitext

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
        self.step_size = 10
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

        self.progress = Progressbar(self, orient=HORIZONTAL, length=200, mode="determinate")
        self.progress.pack()


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
        file.add_command(label="Rename file", command=self.popup_message)
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
        self.folder_details.never_delete_file(self.current_file)
        self.load_next_file()

    def load_next_file(self):
        if self.folder_details:
            next_file = self.folder_details.get_next_file()
            if next_file:
                self.current_file = FileDetails(self, self.folder_details, next_file)
            else:
                self.current_file = FileDetails(self, self.folder_details, "")
            self.current_file.display_details()
            self.progress.step(self.step_size)          # increases length progress bar after going to the next file

    def change_folder(self):                            # not working
        folder_name = filedialog.askdirectory()
        self.select_folder(folder_name)
       # popup = Tk()
       # popup.wm_title("Choose folder")
       # label = Label(popup, text="Please enter the name of the folder you would like to clean up: ")
       # label.pack(side="top", fill="x", pady=10)
       # self.entry = Entry(popup)
       # self.entry.pack()
       # self.select_folder(self.entry.get())

    # startup
    def select_folder(self, folder_path):
        self.folder_details = FolderDetails(folder_path)
        self.load_next_file()
        self.step_size = 200 / self.folder_details.nr_of_files
        self.progress.config(maximum=200, value=self.step_size)

    def popup_message(self):
        self.popup = Tk()
        self.popup.wm_title("Rename file")
        label = Label(self.popup, text="Please enter how you would like to rename the file: ")
        label.pack(side="top", fill="x", pady=10)
        self.entry = Entry(self.popup)
        self.entry.pack()
        button = Button(self.popup, text="Rename", command=self.file_rename)
        button.pack()
        self.popup.mainloop()

    def file_rename(self):
        new_name = self.entry.get()
        path = self.folder_details.path       # 'str' object has no attribute 'splitext' error message
        file_name, file_extension = splitext(path)
        new_name_with_ext = new_name + file_extension
        rename(join(self.folder_details.path, self.current_file.path), join(self.folder_details.path,
                                                                                   new_name_with_ext))
        self.popup.destroy()
        self.load_next_file()
