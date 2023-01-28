from tkinter import Tk, Text, Button 


class App(Tk):
    WIDTH  = 800
    HEIGHT = 600

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.textbox = Text(self)
        self.textbox.grid(row=0, column=0, sticky='nswe')

        self.index = 0
        
        #this is the current line you want to affect
        self.cline = 1
        
        #this represents 5 different times you have gathered line data into a list
        #...via a much more dynamic method
        self.vals = [
            ["id1", "text1", "usertext1"],
            ["id2", "text2", "usertext2"],
            ["id3", "text3", "usertext3"],
            ["id4", "text4", "usertext4"],
            ["id5", "text5", "usertext5"],
        ]
        
        #current line data
        self.data = self.vals[self.index]
        
        Button(self, text="click", command=lambda: self.process(self.data)).grid(row=1, column=0)

    #this represents processing a line of gathered data   
    def process(self, data):
        if data: 
            self.textbox.insert(f'{self.cline}.end', f'{" ".join(data)}\n')
        
        #below is only necessary for this example
        #the equivalents should be done somewhere else
        self.cline += 1
        self.index += 1
        self.data = self.vals[self.index] if self.index < len(self.vals) else None


if __name__ == '__main__':
    app = App()
    app.title("My Application")
    app.geometry(f'{App.WIDTH}x{App.HEIGHT}')
    app.mainloop()

input()