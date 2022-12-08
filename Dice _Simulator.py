import random
from tkinter import *

root = Tk()
root.geometry("900x800")

l1 =Label(root,text='',font = ("arial",300))

def roll():
	# print("This is Dice.")
	number= ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	# (This are Ascii characters for no. 1,2,3,4,5,6)
	l1.config(text=f'{random.choice(number)} {random.choice(number)}')
	l1.pack()

b1=Button(root,text="Roll the Dice",command=roll) #roll is function name

b1.place(x=600,y=10)

# b2=Button(root,text="Print",fg="red")
# b2.pack(side=LEFT)

root.mainloop()
