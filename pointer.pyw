from threading import Thread
import pyautogui as pa
import pynput
from tkinter import *
from tkinter import messagebox
from time import sleep
import os
import ctypes

st="new tile"
def pointToFile(file):
    fil=""
    for x in file:
        if x!=" ":
            fil+=x
    file=fil
    if file in os.listdir(os.getcwd()+"/resources"):
        file=open("resources/"+file,"r")
        mouse_listener = pynput.mouse.Listener(suppress=True)
        mouse_listener.start()
        st=file.read()
        file.close()
        mouse_listener.stop()
        pa.write(st)
    else:
        Tk().withdraw()
        op=messagebox.askyesno(title="Code BLock",message="Not found do you want to create")
        if op:
            os.startfile("updater.pyw")
        

def main():
    file=open("criticalsection","r")
    st=file.read()
    file.close()
    pointToFile(st)

Thread(target=main).start()