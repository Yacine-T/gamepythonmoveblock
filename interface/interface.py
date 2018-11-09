from tkinter import *
from tkinter import ttk

window = Tk()

window.title("Level Editor")

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
windowWidth = 800
windowHeight = 600
windowX = int((screenWidth - windowWidth) / 2)
windowY = int((screenHeight - windowHeight) /2)

window.geometry("{}x{}+{}+{}".format(windowWidth,windowHeight,windowX,windowY))
#window.minsize(640,480)
#window.resiable(width=False,height=False)
#window.positionfrom("programm")

#-----------------------------
label = ttk.Label(window,text = "Hey I'm loosing !")
label.pack()
#-----------------------------
v_txt = StringVar()
line_txt = ttk.Entry(window,textvariable=v_txt,width=30)
line_txt.pack()
#-----------------------------
v_case = IntVar()
case = ttk.Checkbutton(window,text="36",variable=v_case)
case.pack()
#-----------------------------
v_radio = StringVar()
button1 = ttk.Radiobutton(window,text="oui",variable=v_radio,value=1)
button2 = ttk.Radiobutton(window,text="non",variable=v_radio,value=2)
button3 = ttk.Radiobutton(window,text="peut etre",variable=v_radio,value=3)

button1.pack()
button2.pack()
button3.pack()
#-----------------------------
list = Listbox(window)
list.pack()

list.insert(END,"EYASSU")
list.insert(END,"FARES")
list.insert(3,"YACINE")
list.insert(4,"THOMAS")
#-----------------------------
button = ttk.Button(window,text="Exit",command=window.quit)
button.pack()
#-----------------------------
window.mainloop()
#-----------------------------
print("Line text : ",v_txt.get())
print("Case coche ? : ",v_case.get())
print("Choix : ",v_radio.get())
print("Choix dans la liste : ",list.get(list.curselection()))
