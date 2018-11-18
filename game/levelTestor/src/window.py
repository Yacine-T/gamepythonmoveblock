from tkinter import *
from tkinter import ttk
from gridLevel import *
from box import *

class Window(ttk.Frame):

	def __init__(self, win, **kwargs):
		ttk.Frame.__init__(self, win, **kwargs)
		self.pack(fill = BOTH)

		self._gridFrame = self._buildGridFrame()

		self._gridFrame.pack(fill = BOTH)

	def _buildGridFrame(self):
		grid = GridLevel(self)
		return grid
