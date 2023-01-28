
from pynput.keyboard import Key,Listener,HotKey
import pynput
import os
import pyautogui as pa
import ctypes
from time import sleep
from playsound import playsound
import subprocess
from tkinter import *
from tkinter import messagebox
from threading import Thread
index=0
ls=""
st=""
ignoreKeys=Key.caps_lock,[Key.shift,Key.num_lock]
try:
    def run(key):
        #----> vocal statements
        '''playsound("sound.mp3")
        ls=""
        index=0
        subprocess.call("python run.pyw",shell=True)'''
        #------> console application statements
        #keyboard_listener = pynput.keyboard.Listener(suppress=True)
        #keyboard_listener.start()
        print("###########",ls)
        if key==Key.enter:
            global st
            file=open("criticalsection","w+")
            file.write(ls)
            os.startfile("languageProcess.pyw")
            file.close()
            return False

    def take(char,ind):
        global st
        global ls
        global index
        ind=index
        ls+=char
        index+=1
        print(index,char,">>>>>>>",ls)
            
    def filterKey(keyf):  #returns the characters
        if keyf==Key.space:
            return ' '
        return str(keyf)[1]

        
    def on_press(key):
        global index
        global ls
        if key not in ignoreKeys:

            if key==Key.backspace:
                l=[]
                for x in ls:
                    l.append(x)
                try:
                    l.pop()
                except:
                    ls=""
                    index=0
                    print("NULL")
                    return 0
                ls=""
                for x in l:
                    ls+=x
                    print(x)
                index-=1
                print(ls)

            elif key==Key.enter:
                    st=ls
                    print(st)
            else:
                take(filterKey(key),index)
    def mainThread():
        with Listener(on_press=on_press,on_release=run) as listener:
                listener.join()

    root=Tk()
    root.withdraw()
    Thread(target=mainThread).start()  #using thread to enhance the performance
except:
    Tk().withdraw()
    messagebox.showinfo("Code Block",message="The Code Block is terminated due to occurance of some error")
