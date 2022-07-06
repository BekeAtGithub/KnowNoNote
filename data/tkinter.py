# import packages and libraries

#Import OS library
from cProfile import label
import os
#import everything from tkinter
from tkinter import *
#to get the space above the message
from tkinter.messagebox import *
#to get the dialog box to open when required
from tkinter.filedialog import *
class Notepad:
    # set up the root widget
    __root = Tk()
    __thisWidth = 1000
    __thisHeight = 1000
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisCommandMenu = Menu(__thisMenuBar, tearoff=0)
    # to add scrollBar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None
    def __init__(self,**kwargs):
        # icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass
    #set window size as mentioned above (the default is 300x300)
    try:
        self.__thisWidth = kwargs['width']
        except KeyError:
        pass
    try:
        self.__thisHeight = kwargs['height']
        except KeyError:
        pass
        # the window text
        self.__root.title("Untitled-Notepad")
        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        # for left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2)
        # for right-alling
        top = (screenHeight / 2) - (self.__thisHeight / 2)
        # for top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))
        # to make textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        # add controls (widget)
        self.__thisTextArea.grid(sticky = N + E + S + W)
        # to open new file
        self.__thisFileMenu.add_command(label="New")
        # to open an already existing file
        self.__thisFileMenu.add_command(label="Open")
        # to save current file
        self.__thisFileMenu.add_command(label="Save")
        # to create a line in the dialog
        self.__thisFileMenu.addSeperator()
        self.__thisFileMenu.add_command(label="Exit")
    command=self.__quitApplication()
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)
        #to give cut feature
        self.__thisEditMenu.add_command(label="Cut",
    command=self.__cut)
        #to give copy feature
        self.__thisEditMenu.add_command(label="Copy",
    command=self.__copy)
        #to give paste feature
        self.__thisEditMenu.add_command(label="Paste",
    command=self.__paste)
        #to give edit feature
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)
        # to create Application description feature
        self._thisEditMenu.add_command(label="About KnowNoNote",
    command=self.__showAbout)
        # to create Command description feature
        self._thisCommandMenu.add_command(label="About Commands", 
    command=self.__showCommand)
        self.__thisMenuBar.add_cascade(label"Commands", menu=self.__thisCommandMenu)
        self.__thisMenuBar.add_cascade(label"Help", menu=self.__thisHelpMenu)
        self.__root.config(menu=self.__thisMenuBar)
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    def __quitApplication(self):
        self.__root.destroy()
        # exit()
    def __showAbout(self):
        showinfo("about KnowNoNote","Simple Text editor like notepad using Python")
    def __showCommand(self):
        showinfo("KnowNoNote","Just another text editor \n Copyright \n Licensed by Clout Ruler Temple")
    def __openFile(self):
        self.__file == askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            #try to open the file
            #set the window title 
            self.__root.title(os.path.basename(self.__file) + " - KnowNoNote")
            self.__thisTextArea.delete(1.0,END)
            file = open(self.__file,"r")
            self.__thisTextArea.insert(1.0,file.read())
            file.close()
    def __newFile(self):
        if self.__file == None:
            #save as new file
            self.__file == asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")]))
        if self.__file == "":
            self.__file == None
        else:
            #try to save the file
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()
            # change the window title
            self.__root.title(os.path.basename(self.__file) + " - KnowNoNote")
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()
        def __cut(self):
            self.__thisTextArea.even_generate("<<Cut>>")
        def __copy(self):
            self.__thisTextArea.even_generate("<<Copy>>")
        def __paste(self):
            self.__thisTextArea.even_generate("<<Paste>>")
        def run(self):
            #Run Main Application
            self.__root.mainloop()
# Run Main Application
notepad = NotePad(width=600,height=400)
notepad.run()
