from tkinter.messagebox import *
from tkinter.filedialog import *
import pickle

def centerWindow(window,width,height):
	screenWidth = window.winfo_screenwidth()
	screenHeight = window.winfo_screenheight()
	windowX = int((screenWidth - width) / 2)
	windowY = int((screenHeight - height) /2)
	window.geometry("{}x{}+{}+{}".format(width,height,windowX,windowY))

def openLevel(window,root):
	level = window.getLevel()

	if askesno("Save your work", "Do you want to save your work ?") :
		saveAsLevel(level)
	window = Window(root)

def saveLevel(window):
	level = window.getLevel()
	filename = window.getFileName() #TODO configure getFileName in window class and setFileName for saveAsLevel

	file = open(filename,"wb")
	pickle.dump(level,file)
	file.close()

def saveAsLevel(window):
	level = window.getLevel()
	file = asksaveasfile(mode="wb", title="Save level as", defaultextension = ".dat", filetypes = [('data files', '.dat')], initialdir = ".")
	pickle.dump(level,file)
	window.setFileName(file.name)
	file.close()

def undo(window):
	grid = window.getGrid()
	listAction = window.getLastAction()

	if(len(listAction ) > 0):
		lastAction = listAction[len(listAction ) - 1]
		if lastAction[0] == "clear" :
			for i in lastAction[1]:
				grid[i[0]][i[1]].update(i[2])
		else :
			grid[lastAction[0]][lastAction[1]].update(lastAction[2])
		listAction.remove(lastAction)