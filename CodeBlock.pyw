import os
import ctypes
def checkAllFiles():
    li=[]
    files=os.listdir(os.getcwd())
    print(files)
    ch=['cliprunner', 'code block.mp3', 'CodeBlock.pyw', 'criticalsection', 'KeyListener.pyw', 'languageProcess.pyw', 'pointer.pyw', 'requestListener.pyw','resources']
    for x in ch:
        if x not in files:
            li.append(x)
    if len(li)!=0:
        st=""
        for x in li:
            st+=" \n"+x
        if ctypes.windll.user32.MessageBoxW(0, "The files are missing try to contact with developer"+st, "Code Block", 5)==4:
            checkAllFiles()
        return False
    return True
if checkAllFiles():
    os.startfile("KeyListener.pyw")