from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from box import *
from util import *
import pickle

class GridLevel(ttk.Frame):

	def __init__(self, window, **kwargs):
		ttk.Frame.__init__(self, window, **kwargs)
		self._level = buildLevel(openLevel(), self)
		self._grid = self._buildGrid()

	def getLevel(self):
		return self._level

	def changeLevel(self, level):
		self._level = level
		self._grid = _buildGrid()

	def _buildGrid(self):
		grid = []
		for i in range(len(self._level)):
			grid.append([])
			for j in range(len(self._level[i])):
				grid[i].append(self._level[i][j])
				grid[i][j].grid(row = i, column = j)
		return grid
