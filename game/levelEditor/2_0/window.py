from tkinter import *
from tkinter import ttk
from gridLevel import *
from typeMenu import *

class Window(ttk.Frame):

	def __init__(self, win, **kwargs):
		ttk.Frame.__init__(self, win, **kwargs)
		self.pack(fill = BOTH)

		self._boxTypeSelected = IntVar()

		self._menuFrame = self._buildMenuFrame()
		self._gridFrame = self._buildGridFrame()

		self._menuFrame.pack(side = RIGHT)
		self._gridFrame.pack(side = LEFT)

	def _buildGridFrame(self):
		grid = GridLevel(self, self._boxTypeSelected)
		return grid

	def _buildMenuFrame(self):
		menu = TypeMenu(self, self._boxTypeSelected)
		return menu

	def clearGrid(self):
		self._gridFrame.clearGrid()

	def getLevel(self):
		return self._gridFrame.getLevel()

	def getLastAction(self):
		return self._gridFrame.getLastAction()

	def getGrid(self):
		return self._gridFrame.getGrid()

	def getFileName(self):
		return self._gridFrame.getFileName()

	def setFileName(self, fileName):
		self._gridFrame.setFileName(fileName)