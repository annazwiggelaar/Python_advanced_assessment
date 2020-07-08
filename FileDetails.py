import os
from os.path import exists, join, getsize
from tkinter import *
from PIL import ImageTk, Image
import time
import winsound


class FileDetails():

    def __init__(self, cleanUpGui, folder, path):
        self.gui = cleanUpGui
        self.folder = folder
        self.path = path
        self.picture = None

    def display_details(self):
        if self.path != "" and exists(join(self.folder.path, self.path)):
            self.gui.current_file_name.configure(text="file name: " + self.path)
            file_size = getsize(join(self.folder.path, self.path))
            self.gui.current_file_size.configure(text="file size: " + str(file_size))
            self.gui.deleted_count.configure(text="number of deleted files: " + str(self.gui.del_count))
            self.gui.deleted_bytes_count.configure(text="deleted bytes: " + str(self.gui.del_bytes_count))
            file_name, file_extension = os.path.splitext(self.path)
            if file_extension == ".txt":
                file = open(join(self.folder.path, self.path))
                first_line = file.readline()
                self.gui.current_file_preview.configure(text="preview: " + str(first_line))
            elif file_extension == ".jpg" or file_extension == ".png":
                pic = Image.open(join(self.folder.path, self.path))
                self.picture = ImageTk.PhotoImage(pic)
                self.gui.current_file_pic_preview.configure(image=self.picture)
            elif file_extension == ".wav":
                file = join(self.folder.path, self.path)
                winsound.PlaySound(file, winsound.SND_ASYNC)
                time.sleep(5)
                winsound.PlaySound(None, winsound.SND_ASYNC)
                self.gui.current_file_preview.configure(text="preview: you just heard the first 5 seconds of "
                                                             + str(self.path))
            else:       # if file is not one of above file types
                self.gui.current_file_preview.configure(text="preview: not available for this file type")
        else:
            self.gui.folder_empty.configure(text="Congratulations, you have cleaned this folder!")
            self.gui.current_file_name.configure(text="file name: <no file selected>")
            self.gui.current_file_size.configure(text="file size: <no file selected>")
            self.gui.current_file_preview.configure(text="preview: <no file selected>")
