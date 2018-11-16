from sense_hat import SensHat

sense = SensHat()

class Player:

    def __init__(self,position):
        posx = 0
        posy = 0

    def getposx(self):
        return posx
    def getposx(self):
        return posy

    def setpos(self,posx,posy) :
        position = (posx,posy)
        #sense.set_pixel(posx,posy,(255,255,255))

    def move(self,event):
    if event.action == 'held' and event.direction =='right':
        direction= 1;
        #next_position = getposx+1,getposy
        if (!cantpasswall):
            setpos(posx+1,posy)
    if event.action == 'held' and event.direction =='left':
            direction = -1;
            setpos(posx-1,posy)
    if event.action == 'held' and event.direction =='up':
        direction = 2;
        setpos(posx,posy+1)
    if event.action == 'held' and event.direction =='down':
        direction= -2;
        setpos(posx,posy-1)

    def cantpasswall(self,next_position):
        if (led.isWall(next_position)):
            return false



        if (led.next() == 1 and direction == 1):


        if (led.next() == 1 and direction == 1):
