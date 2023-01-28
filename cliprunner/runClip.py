from pyperclip import paste
file=open("cliprunner.py","w")
file.write(paste())
file.close
file=open("cliprunner.py","a")
file.write("\ninput()")
file.close()
import os 
os.system("python cliprunner.py")
print("sathwik")