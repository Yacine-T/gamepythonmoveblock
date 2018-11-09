from tkinter import *
from tkinter import ttk

class TypeMenu(ttk.Frame):

	def __init__(self, window, boxTypeSelected, **kwargs):
		ttk.Frame.__init__(self, window, **kwargs)
		self._parent = window
		r = self._buildBoxTypeSelection(boxTypeSelected)
		self._resetGrid = ttk.Button(self, text = "reset", command = self._resetGrid)
		self._resetGrid.grid(sticky = "W", row = r+1, column = 0)

	def _buildBoxTypeSelection(self, boxTypeSelected):
		boxType = [	["air",0],
					["wall",1],
					["movable box",10],
					["player",50],
					["end",100]]
		j = 0
		for i in boxType :
			ttk.Radiobutton(self,text = i[0], variable = boxTypeSelected, value = i[1]).grid(sticky = "W", row = j, column = 0)
			j += 1
		return j

	def _resetGrid(self):
		self._parent.clearGrid()