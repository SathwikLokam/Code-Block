import tkinter as tk
from tkinter import messagebox

# Top level window
frame = tk.Tk()
#frame.withdraw
frame.title("TextBox Input")
frame.geometry('500x230')

def writer():
    file=open("resources/"+str(nmu.get(1.0, "end-1c")),"w")
    file.write(str(res.get(1.0, "end-1c")))
    print(nmu.get(1.0, "end-1c"),res.get(1.0, "end-1c"))

    file.close()
    lbl.config(text ="Resource updated")

# TextBox Creation
nmu = tk.Text(frame,
                   height = 1,
                   width = 50)
res = tk.Text(frame,
                   height = 10,
                   width = 50)

  
nmu.pack()
res.pack()
# Button Creation
writer = tk.Button(frame,
                        text = "commit", 
                        command = writer)
writer.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
#frame.withdraw()
frame.mainloop()