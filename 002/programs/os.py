from kernel import *
from config import *
from pyrun import *
import tkinter


def runConfig():
    pyrun('programs/tkConfig.py')

window = tkinter.Tk()
window.title(title)
window.geometry(set1)


settings = tkinter.Button(text="Settings",command=runConfig , bg = background, bd = border ).pack()


window.mainloop()

