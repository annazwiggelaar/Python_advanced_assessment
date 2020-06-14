from tkinter import *

from CleanUpGui import CleanUpGui

root = Tk()
root.geometry("300x300")
cleanup = CleanUpGui(root)
# messy folder should be a sub-folder in your project.
cleanup.select_folder("messy_folder/")

root.mainloop()


