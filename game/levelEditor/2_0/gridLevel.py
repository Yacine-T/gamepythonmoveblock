from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from boxLevel import *
import pickle

class GridLevel(ttk.Frame):

	def __init__(self, window, boxTypeSelected, **kwargs):
		ttk.Frame.__init__(self, window, **kwargs)
		self._lastAction = []
		self._level , self._fileName = self._loadLevel()
		self._grid = self._buildGrid(boxTypeSelected)

	def clearGrid(self):
		self._lastAction.append(["clear",[]])
		for i in range(len(self._grid)):
			for j in range(len(self._grid[i])):
				if self._level[i][j] != 0 :
					self._lastAction[len(self._lastAction) - 1][1].append([i, j, self._level[i][j]])
					self._grid[i][j].update(0)

	def getLevel(self):
		return self._level

	def getLastAction(self):
		return self._lastAction

	def getGrid(self):
		return self._grid

	def getFileName(self):
		return self._fileName

	def setFileName(self, filename):
		self._fileName = filename

	def _loadLevel(self):
		filename = askopenfilename( title="Open a level", filetypes = [('dat files','.dat')], initialdir = ".")
		file = open(filename, "rb")
		level = pickle.load(file)
		file.close()
		return level , filename

	def _buildGrid(self, boxTypeSelected):
		grid = []
		for i in range(len(self._level)):
			grid.append([])
			for j in range(len(self._level[i])):
				grid[i].append(BoxLevel(self, i, j, self._level, self._lastAction, self._level[i][j], boxTypeSelected))
				grid[i][j].grid(row = i, column = j)
		return grid
				