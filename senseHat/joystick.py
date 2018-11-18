from sense_emu import *
# from sense_hat import *


class Joystick:

    def __init__(self,hat,player,mode):
        self._hat = hat
        self._stick = hat.stick

        self._stick.direction_any = self.move

        self._player = player

        self._mode = mode

        #event call when joystick is moved
        #call move function of player with direction parameter (left, right, up or down)
    def move(self,event):
        if self._mode == 'playing' :
            if event.action in (ACTION_PRESSED, ACTION_HELD):
                if event.direction in ('up', 'down', 'left', 'right'):
                    self._player.move(event.direction)
                else : #event.direction = 'middle'
                    self._player.use()
        elif self._mode == '' :
