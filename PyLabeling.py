from tkinter import *
  
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master
        self.option_add('*Font', '19')
        # widget can take all window
        self.pack(fill=BOTH, expand=1)


        ButtonArr = [0 for y in range(5)]
        for y in range(5):
            ButtonArr[y] = Button(self)
            ButtonArr[y].grid(column = 0, row = y)
        AddButton = Button(self, text="+", command=self.AddCategory)
        
        # place button at (0,0)
        AddButton.grid(column=0, row=len(ButtonArr))
    def AddCategory(self):
        pass
root = Tk()
app = Window(root)
root.wm_title("Button Test")
root.geometry("320x320")
root.mainloop()