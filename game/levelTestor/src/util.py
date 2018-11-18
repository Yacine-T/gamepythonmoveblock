from tkinter.messagebox import *
from tkinter.filedialog import *
from box import *
import pickle

def centerWindow(window,width,height):
	screenWidth = window.winfo_screenwidth()
	screenHeight = window.winfo_screenheight()
	windowX = int((screenWidth - width) / 2)
	windowY = int((screenHeight - height) /2)
	window.geometry("{}x{}+{}+{}".format(width,height,windowX,windowY))

def undo(window):
	grid = window.getGrid()
	window.back()

	if(len(listAction ) > 0):
		lastAction = listAction[len(listAction ) - 1]
		if lastAction[0] == "clear" :
			for i in lastAction[1]:
				grid[i[0]][i[1]].update(i[2])
		else :
			grid[lastAction[0]][lastAction[1]].update(lastAction[2])
		listAction.remove(lastAction)

def openLevel():
    fileName = askopenfilename( title="Open a level", filetypes = [('dat files','.dat')], initialdir = ".")
    file = open(fileName,"rb")
    data = pickle.load(file)
    file.close()
    return data

def buildLevel(data, window):
    level = []
    i = 0
    for line in data:
        level.append([])
        j = 0
        for box in line:
            if(box != 50):
                type = {
        			0: Air(window),
        			1: Wall(window),
        			10: MovableBlock(window),
                    100: End(window)
                    }.get(box,Air(window))
                level[i].append(type)
            else :
                #if is player create player and set air at is position
                #Player(i,j)
                level[i].append(Air(window))
            j += 1
        i += 1
    return level
