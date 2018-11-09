from tkinter import *
import pickle


def readLevel(lvl) :
    input = open("level{0}.dat".format(lvl),"rb")
    data = pickle.load(input)
    print(data)
    input.close()
    return data

def buildLeftFrame(f,lvl) :
    leftFrame = Frame(f,borderwidth=2)
    leftFrame.pack(side=LEFT)
    for line in range(8):
        for col in range(8):
            Button(leftFrame,text=lvl[line][col],relief=FLAT).grid(row=line,column=col)
    leftFrame

def buildRightFrame(f):
    rightFrame = Frame(f,borderwidth=2)
    rightFrame.pack(side=RIGHT)
    Button(rightFrame,text="Save",command=savelvl).pack()


data = readLevel(1)

fen = Tk()


leftFrame = buildLeftFrame(fen,data)
rightFrame = buildRightFrame(fen)




fen.mainloop()
