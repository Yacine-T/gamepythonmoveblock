from tkinter import *
from tkinter import ttk
from util import *
from window import *

root = Tk()
root.title("Level Editor")
centerWindow(root, 800, 650)

menuBar = Menu(root)

menuFile = Menu(menuBar, tearoff = 0)
#menuFile.add_command(label = "Open", command = lambda : openLevel(window))
menuFile.add_command(label = "Save", command = lambda : saveLevel(window))
menuFile.add_command(label = "Save as", command = lambda : saveAsLevel(window))
menuBar.add_cascade(label = "File", menu = menuFile)

menuEdit = Menu(menuBar, tearoff = 0)
menuEdit.add_command(label = "Undo", command = lambda : undo(window))
menuBar.add_cascade(label = "Edit", menu = menuEdit)

root["menu"] = menuBar

window = Window(root)

window.mainloop()
