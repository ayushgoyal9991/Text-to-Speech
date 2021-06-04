# -*- coding: utf-8 -*-
"""

@author: Ayush
"""

import pyttsx3
from tkinter import *

root = Tk()
root.geometry("350x350")
root.configure(bg='ghost white')
root.title("Test to Speech")

Label(root,text="Text to Speech",font="arial 20 bold",bg='white smoke').pack()
msg = StringVar()
Label(root,text="Enter Text",font='arial 15 bold',bg='white smoke').place(x=20,y=60)
entry_field = Entry(root,textvariable=msg,width='50')
entry_field.place(x=20,y=100)

def Text_to_Speech():
    message = entry_field.get()
    engine = pyttsx3.init()
    engine.say(str(message))
    engine.runAndWait()
    
def Exit():
    root.destroy()
    
def Reset():
    msg.set("")
    
Button(root,text="Play",font='arial 15 bold',command=Text_to_Speech,width='4').place(x=25,y=140)
Button(root,text="Exit",font='arial 15 bold',command=Exit,width='4').place(x=100,y=140)
Button(root,text="Reset",font='arial 15 bold',command=Reset,width='4').place(x=175,y=140)

root.mainloop()