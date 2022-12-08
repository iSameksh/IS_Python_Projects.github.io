from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
# from pyparsing import Word

def change(text="type",src="English",dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_source.get()
    d = comb_dest.get()
    msg = source_txt.get(1.0,END)
    textget = change(text= msg, src = s, dest = d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)





root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='GREY')

lab_txt = Label(root,text= "Translator", font=("Time New Roman", 20 , "bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text= "Source Text", font=("Time New Roman", 18 , "bold"),fg='WHITE', bg='BLACK')
lab_txt.place(x=100,y=100,height=22,width=300)

source_txt = Text(frame , font=("Time New Roman", 20 , "bold"), wrap=WORD)
source_txt.place(x=10,y=130,height=150,width=480)

list_text = list(LANGUAGES.values())

comb_source = ttk.Combobox(frame,value=list_text)
comb_source.place(x=10,y=300,height=40,width=150)
comb_source.set("english")

button_change = Button(frame,text="Translate",relief = RAISED , command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=50,width=150)
comb_dest.set("english")

lab_txt = Label(root,text= "Destination Text", font=("Time New Roman", 18 , "bold"),fg='WHITE', bg='BLACK')
lab_txt.place(x=100,y=360,height=22,width=300)

dest_txt = Text(frame , font=("Time New Roman", 20 , "bold"), wrap=WORD )
dest_txt.place(x=10,y=400,height=150,width=480)
# dest_txt.pack(padx=10,pady=10)

root.mainloop()

