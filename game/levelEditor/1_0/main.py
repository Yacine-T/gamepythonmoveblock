from tkinter import *
from tkinter import ttk
import interface

fen = Tk()
fen.title("Level Editor")
interface = interface.Interface(fen)

interface.mainloop()