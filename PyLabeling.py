from tkinter import *
from tkinter.colorchooser import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.color = '#d9d9d9'
        self.master = master
        self.option_add('*Font', '19')
        self.pack(fill=BOTH, expand=1)

        #declaring the Top Level Window
        self.newWindow = Toplevel()
        self.newWindow.destroy()
        
        self.ButtonArr = []

        self.AddButton = Button(self, text="+", command=self.CreateCategory)
        self.AddButton.grid(column=0, row=len(self.ButtonArr))

        
        self.MenuBar()
    def MenuBar(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Open", command=self.open_Image)
        menu.add_cascade(label="File", menu=file)

    def CreateCategory(self):
        
        if Toplevel.winfo_exists(self.newWindow):
            self.newWindow.destroy()
        self.newWindow = Toplevel(self)
        self.newWindow.wm_title("Create a new Category")
        self.newWindow.geometry("400x330")
        self.newWindow.option_add('*Font', '19')
        L1 = Label(self.newWindow, text="Label")
        L1.pack(side=LEFT)
        self.E1 = Entry(self.newWindow, bd=5, font=("Arial", 14))
        self.E1.pack(side=RIGHT)
        self.ColerChooser = Button(self.newWindow,text="Select Color" ,command=self.getColor).pack(side=TOP)
        
        self.ok = Button(self.newWindow, text="Confirm",command = self.AddCategory, bg='green').pack(side=BOTTOM)
        
        
    def getColor(self):
        self.color = askcolor()
        self.newWindow.configure(background=self.color[1])

    def AddCategory(self):
        
        self.ButtonArr.append(Button(self, text=self.E1.get(), bg=self.color[1]))
        self.AddButton.grid(column=0, row=len(self.ButtonArr) + 1)

        self.ButtonArr[len(self.ButtonArr) - 1].grid(column=0,row=len(self.ButtonArr))
    def open_Image(self):
        pass
        
root = Tk()
app = Window(root)
root.wm_title("Button Test")
root.minsize(640, 480)
root.geometry("640x480")
root.mainloop()
