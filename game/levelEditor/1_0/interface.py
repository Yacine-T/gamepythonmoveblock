from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
import pickle
class Interface(Frame):

    def __init__(self,fen,**kwargs):
        f=Frame.__init__(self,fen,width=768,height=576,**kwargs)
        self.pack(fill=BOTH)

        self.filename = askopenfilename( title="Ouvrir un level",
                                    filetypes=[('dat files','.dat')],
                                    initialdir=".")
        fichier = open(self.filename,"rb")
        self.level = pickle.load(fichier)
        fichier.close()

        self.color = [[0,'white'],
                      [1,'black'],
                      [10,'orange'],
                      [50,'blue'],
                      [100,'green']]

        self.leftFrame = Frame(self,borderwidth=2)
        self.leftFrame.pack(side=LEFT)
        self.buildLeftFrame(self.level)

        self.rightFrame = Frame(self,borderwidth=2)
        self.rightFrame.pack(side=RIGHT)
        self.buildRightFrame()

    def buildLeftFrame(self,lvl) :
        i = 0
        while i < len(lvl):
            j = 0
            while j < len(lvl[i]):
                color = {
                    0:'white',
                    1:'black',
                    10:'orange',
                    50:'blue',
                    100:'green'
                }.get(lvl[i][j],"purple")
                Button(self.leftFrame,text=str(lvl[i][j]),relief=FLAT, height=5, width=10, bg=color,fg=color, command=lambda:self.upNumber(i,j)).grid(row=i,column=j)
                j+=1
            i+=1

    def buildRightFrame(self):
        Button(self.rightFrame,text="Save",command=self.savelvl, font=('Helvetica', '20')).pack()

    def upNumber(self,i,j):
        self.level[i][j] = {
                    0:1,
                    1:10,
                    50:100,
                    100:0
        }.get(self.level[i][j],0)
        print(self.level[i][j])

    def savelvl(self):
        output = open(self.filename, "wb")
        pickle.dump(self.level, output)
        output.close()
