from threading import Thread
import pyautogui as pa
import pynput
from tkinter import *
from tkinter import messagebox
from time import sleep
import os
import json

st="new tile"
def pointToFile(file):
    dic=file
    file=dic["key"].strip()
    operations=dic["operation"]
    if file+".json" in os.listdir(os.getcwd()+"/resources"):
        file=open("resources/"+file+".json","r")
        mouse_listener = pynput.mouse.Listener(suppress=True)
        mouse_listener.start()
        st=json.load(file)
        file.close()
        mouse_listener.stop()
        for x in operations:
            pa.write("\n#"+x+" -> \n"+st[x])
            pa.press("enter")
    else:
        Tk().withdraw()
        op=messagebox.askyesno(title="Code BLock",message="Not found do you want to create")
        if op:
            os.startfile("updater.pyw")
        
def main():
    file=open("criticalsection","r")
    st=json.load(file)
    file.close()
    pointToFile(st)

Thread(target=main).start()

