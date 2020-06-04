from tkinter import *

from CleanUpGui import CleanUpGui

root = Tk()
cleanup = CleanUpGui(root)
# messy folder should be a sub-folder in your project.
cleanup.select_folder("messy_folder/")

root.mainloop()