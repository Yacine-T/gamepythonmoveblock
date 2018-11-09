from tkinter import *


class BoxLevel(Canvas):

	def __init__(self, window, i, j, level, lastAction, boxTypeInitial, boxTypeSelected, **kwargs):
		Canvas.__init__(self, window, width = 75, height = 75, **kwargs)

		self["bg"] = self._setColor(boxTypeInitial)
		self._boxTypeSelected = boxTypeSelected
		self._i = i
		self._j = j
		self._level = level
		self._lastAction = lastAction
		self.bind("<Button-1>",self._click)


	def _click(self, event):
		self._lastAction.append([self._i, self._j, self._level[self._i][self._j]])
		self._level[self._i][self._j] = self._boxTypeSelected.get()
		self["bg"] = self._setColor(self._boxTypeSelected.get())

	def update(self,boxType):
		self._level[self._i][self._j] = boxType
		self["bg"] = self._setColor(boxType)

	def _setColor(self, boxType):
		return {
			0:"white",
			1:"black",
			10:'orange',
            50:'blue',
            100:'green'}.get(boxType,"purple")