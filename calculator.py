from cgitb import text
from tkinter import *

import click
 
def click(event):
    global scvalue
    text= event.widget.cget("text")
    # print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()


    elif text == "C":
        scvalue.set("")
        scvalue.update()
    
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()

root.geometry("2000x1000")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, ipady=10, padx=10, pady=10) 


f = Frame(root, bg="grey")
b = Button(f, text="9" , padx="7",pady="8",font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="8" , padx="7",pady="8" ,font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="7" , padx="7",pady="8" ,font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="+" , padx="7",pady="8",font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="6" ,  padx="7",pady="8",font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="5" ,  padx="7",pady="8",font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="4" , padx="7",pady="8" ,font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="-" ,  padx="7",pady="8",font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="3" ,  padx="7",pady="8" ,font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="2" ,  padx="7",pady="8" ,font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="1" ,  padx="7",pady="8",font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="*" ,  padx="7",pady="8" ,font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

f.pack()


f = Frame(root, bg="grey")
b = Button(f, text="0" , padx="7",pady="8" ,font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="=" ,  padx="7",pady="8" ,font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="C" ,  padx="7",pady="8" ,font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

b = Button(f, text="/" , padx="7",pady="8" ,font="lucida 35 bold")
b.pack(side=LEFT, padx="8", pady="5")
b.bind("<Button-1>", click)

f.pack()


root.mainloop()






