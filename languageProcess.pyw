import sys
from tkinter import *
from tkinter import messagebox
from threading import Thread
import os

def  ignoreStrings(strs):
    ignoreList=[
        "i",
        "want",
        "loop",
        "what",
        "need",
        "python",
        "get",
        "me",
        "a",
        "explain",
        "defination",
        "example",
        "define",
        "example",
        "syntax"
    ]
    if "explain" in strs:
        ese="explain"
    elif ("defination" in strs) or ("define" in strs):
        ese="defination"
    elif "example" in strs:
        ese="example"
    else:
        ese="syntax" 
    
    filteredList=[]
    for st in strs:
        if st not in ignoreList:
            filteredList.append(st)
    ss=""
    for x in filteredList:
        ss+=x
        ss+=" "

    ##################
    file=open("criticalsection","w")
    file.write(ss)
    file.close()
    os.startfile("pointer.pyw")
    ################

def convert():
    file=open("criticalsection","r")
    st=file.read().split()
    strs=""
    
    for w in st:
        for x in w:
            strs+=x.lower()
        strs+=" "
    file.close()
    return strs
def main():
    strs=ignoreStrings(list(map(str,convert().split())))
Thread(target=main).start()

