from tkinter import *

class Box(Canvas):

    def __init__(self, isMovable, isSolid, color, window):
        Canvas.__init__(self, window, width = 95, height = 95)
        self._isMovable = isMovable
        self._isSolid = isSolid
        self._color = color
        self["bg"] = "#{0:02x}{1:02x}{2:02x}".format(self._color[0], self._color[1], self._color[2])

    def isMovable(self):
        return self._isMovable

    def isSolid(self):
        return self._isSolid

    def getColor(self):
        return self._color

class MovableBlock(Box):
    def __init__(self, window):
        Box.__init__(self, True, True, (255,255,0), window)

class Air(Box):
    def __init__(self, window):
        Box.__init__(self,False, False, (0,0,0), window)

class End(Box):
    def __init__(self, window):
        Box.__init__(self, False, False, (0,255,0), window)

class Wall(Box):
    def __init__(self, window):
        Box.__init__(self, False, True, (200,200,200), window)
