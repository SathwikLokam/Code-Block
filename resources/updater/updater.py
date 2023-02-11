import os 
import json
import tkinter
from tkinter import *
from tkinter import Text
files=os.listdir(os.getcwd())

for fi in files:
    if fi !="updater.py":
        r=Tk()
        r.title("Updater")
        Label(text=fi,font=("Arial",20)).pack()
        op=open(fi,"r")
        data=json.load(op)
        op.close()
        me = Text(r,
                        height = 10,
                        width = 80)
        sy = Text(r,
                        height = 10,
                        width = 80)
        ex = Text(r,
                        height = 15,
                        width = 80)
        Label(text="Meaning",font=("Arial",15)).pack()   
        me.pack()
        Label(text="Syntax",font=("Arial",15)).pack()
        sy.pack()
        Label(text="Example",font=("Arial",15)).pack()
        ex.pack()
        print(fi)
        def fun():

            data["meaning"]=me.get(1.0, "end-1c")
            data["syntax"]=sy.get(1.0, "end-1c")
            data["example"]=ex.get(1.0, "end-1c")
            print(data)
            json.dump(data,open(fi,"w"))
            r.destroy()

        b=Button(r,text="Update",command=fun,width=60,height=2,background=("green"),font=("Arial",12)).pack()
        mainloop()