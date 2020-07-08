from tkinter import *

from CleanUpGui import CleanUpGui

root = Tk()
root.geometry("400x400")
cleanup = CleanUpGui(root)
# messy folder should be a sub-folder in your project.

cleanup.select_folder("messy_folder/")

root.mainloop()
