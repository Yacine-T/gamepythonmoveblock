from sense_emu import *
# from sense_hat import *


# AXES :
# 0 1 2 3 4 5 6 7 -> X
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# -> Y

class Screen:

    def __init__(self, hat):
        self._hat = hat

    def updateScreen(self,pixels):
        self._hat.clear()
        self._hat.set_pixels(pixels)
