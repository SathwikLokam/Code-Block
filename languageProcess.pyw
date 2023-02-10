import sys
from tkinter import *
from tkinter import messagebox
from threading import Thread
import os
import json

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
        "syntax",
        "and",
        "meaning",
        "is",
        "give",
        "me",
        "hey",
        "just",
        "there",
        "of"
    ]
    ese=[]
    if "explain" in strs:
        ese=[]
    if ("meaning" in strs) or ("meaning" in strs):
        ese.append("meaning")
    if "syntax" in strs:
        ese.append("syntax")
    if "example" in strs:
        ese.append("example")
    if ese==[]:
        print(ese,strs)
        ese.append("meaning")
        ese.append("syntax")
        ese.append("example")
    

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
    dic={}
    dic["key"]=ss
    dic["operation"]=ese
    print(dic)
    json.dump(dic,file)
    file.close()
    os.startfile("pointer.pyw")
    ##################

def convert():
    file=open("criticalsection","r")
    st=file.read().replace(","," ").split()
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

