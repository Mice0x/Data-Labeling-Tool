from tkinter import *
from tkinter.colorchooser import *
from PIL import ImageTk, Image
import PIL
from tkinter import filedialog
import os


class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.color = '#d9d9d9'

        self.option_add('*Font', '19')
        self.pack(fill=BOTH, expand=1)

        # declaring the Top Level Window
        self.newWindow = Toplevel()
        self.newWindow.destroy()

        self.ButtonArr = []

        self.AddButton = Button(self, text="+", command=self.CreateCategory)
        self.AddButton.grid(column=0, row=len(self.ButtonArr))

        self.MenuBar()

        self.bind('<Motion>', self.motion)
        self.bind("<ButtonPress-1>", lambda event: self.capture(True))
        self.bind("<ButtonRelease-1>", lambda event: self.capture(False))
        self.click = False

        self.startPoint = NONE
        self.endPoint = None

        self.directory = ""
        self.current_image_index = 0
        #self.img = Label()

    def MenuBar(self):
        """Creates A Menu Button on the Menu Bar"""
        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)
        file.add_command(label="Open", command=self.open_Image)
        menu.add_cascade(label="File", menu=file)

    def CreateCategory(self):
        """Opens A Window to create a New Category"""
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
        self.ColerChooser = Button(
            self.newWindow, text="Select Color", command=self.getColor).pack(side=TOP)

        self.ok = Button(self.newWindow, text="Confirm",
                         command=self.AddCategory, bg='green').pack(side=BOTTOM)

    def getColor(self):
        """Asks the color for the category Button"""
        self.color = askcolor()
        self.newWindow.configure(background=self.color[1])

    def AddCategory(self):
        """Adds A new Button to select a category"""
        self.ButtonArr.append(
            Button(self, text=self.E1.get(), bg=self.color[1]))
        self.AddButton.grid(column=0, row=len(self.ButtonArr) + 1)

        self.ButtonArr[len(self.ButtonArr) - 1].grid(column=0,
                                                     row=len(self.ButtonArr))

    def open_Image(self):
        """Selecting the path where the Images are Located"""

        self.directory = filedialog.askdirectory(
            initialdir='/', title="Select directory")
        self.files_in_directory = os.listdir(self.directory)

        load = Image.open(self.directory + '/' +
                          self.files_in_directory[self.current_image_index])
        maxsize = (1500, 1028)
        load.thumbnail(maxsize, PIL.Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        self.img = Label(self, image=render)
        self.img.image = render

        self.img.grid(rowspan=28, row=0, column=1, columnspan=27)
        print(self.img.winfo_rootx(), self.img.winfo_rooty())

        self.previusItem = Button(self, text="<", command=self.previus_Image)
        self.previusItem.grid(column = 13, row = 29)

        self.NextItem = Button(self, text=">", command=self.next_Image)
        self.NextItem.grid(column = 14, row = 29)
        

    def change_Image(self):
        
        self.img.grid_forget()
        load = Image.open(self.directory + '/' +
                          self.files_in_directory[self.current_image_index])
        maxsize = (1500, 1028)
        load.thumbnail(maxsize, PIL.Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        self.img = Label(self, image=render)
        self.img.image = render

        self.img.grid(rowspan=28, row=0, column=1)
    def previus_Image(self):
        if self.current_image_index != 0:
            self.current_image_index -= 1
            self.change_Image()
    def next_Image(self):
        if self.current_image_index < len(self.files_in_directory):
            self.current_image_index += 1
            self.change_Image()
    def capture(self, click):
        """Captures mouse click"""
        self.click = click

    def motion(self, event):
        """Captures motion when mouse is clicked"""
        self.x = 0
        self.y = 0

        self.x, self.y = int(event.x), int(event.y)
        #print('x={}, y={}'.format(self.x, self.y))

        if self.click == True and self.startPoint == None:
            self.startPoint = (self.x, self.y)
        elif self.click == False and self.startPoint != None:
            self.endPoint = (self.x, self.y)
            # self.draw_rect()
            print(self.startPoint, self.endPoint)
            self.startPoint = None

    def draw_rect(self):
        pass
        #canvas = Canvas(width=abs(self.startPoint[0]- self.endPoint[0]), height=abs(self.startPoint[1]- self.endPoint[1]), bg='white')
        #canvas.place(x=self.startPoint[0], y=self.startPoint[1])

        #canvas.create_rectangle(self.startPoint[0], self.startPoint[1], self.endPoint[0], self.endPoint[1], width=5, fill='red')
    def get_file_in_directroy(self):
        pass


root = Tk()
app = MainWindow(root)
root.wm_title("DL Tool")
root.minsize(640, 480)
root.geometry("640x480")
root.mainloop()
