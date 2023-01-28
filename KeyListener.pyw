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
st="buddy"
ignoreKeys=[Key.caps_lock,Key.shift,Key.num_lock]
try:
    def run():
        #----> vocal statements
        '''playsound("sound.mp3")
        ls=""
        index=0
        subprocess.call("python run.pyw",shell=True)'''
        #------> console application statements
        
        mouse_listener = pynput.mouse.Listener(suppress=True)
        mouse_listener.start()
        #keyboard_listener = pynput.keyboard.Listener(suppress=True)
        #keyboard_listener.start()
        global st
        for x in range(len(st)):
            pa.write("\b") 
        pa.write("#request>")
        mouse_listener.stop()
        os.startfile("requestListener.pyw")
        # keyboard_listener.stop()

    def exitCode(key):
        if key==Key.esc:
            return ctypes.windll.user32.MessageBoxW(0,"Hey, do you want to exit CodeBlock", "Code Block", 4)==7 or ctypes.windll.user32.MessageBoxW(0, "Code Block terminated", "Code Block", 0)!=1

    def check(char,ind):
        global st
        global ls
        global index
        index=ind%len(st)
        ind=index
        print(index,char)
        if char==st[ind]:
            ls+=char
            index+=1
        else:
            ls=""
            index=0
        if ls==st:
            run()
            
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
            else:
                check(filterKey(key),index)
    def mainThread():
        with Listener(on_press=on_press,on_release=exitCode) as listener:
                listener.join()

    root=Tk()
    root.withdraw()
    playsound("code block.mp3")
    messagebox.showinfo("Code Block",message="Code BLock launched")
    Thread(target=mainThread).start()  #using thread to enhance the performance
except:
    Tk().withdraw()
    messagebox.showinfo("Code Block",message="The Code Block is terminated due to occurance of some error")
 