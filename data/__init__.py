## initialize GUI
##root widget
from tkinter.scrolledtext import ScrolledText


root = Tk()
root.title('KnowNoNote')
root.resizeable(0, 0)

#creating scrollable notepad window
notepad = ScrolledText(root, width = 90, height = 40)
fileName = ' '

