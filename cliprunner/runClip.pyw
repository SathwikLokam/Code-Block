from pyperclip import paste
file=open("cliprunner.py","w")
file.write(paste()+"\ninput()")
file.close()
import os 
os.system("python cliprunner.py")