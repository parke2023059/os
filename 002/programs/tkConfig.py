from config import *
from pyrun import *
import tkinter
#import json






def reload():
    pyrun('programs/tkConfig.py')
    exit()






window = tkinter.Tk()
window.title(settings)
window.geometry(set1)



title = tkinter.Label(text = "Title: " +  title).pack()


colors = tkinter.Label(text ='Button Colors').pack()
red = tkinter.Button(text="Red",command= "", bg = background, bd = border, height = height, width = width ).pack()
blue = tkinter.Button(text="Blue",command= "", bg = background, bd = border, height = height, width = width).pack()
button = tkinter.Button(text="Green",command= "", bg = background, bd = border, height = height, width = width ).pack()
button = tkinter.Button(text="Purple",command= "", bg = background, bd = border, width = width, height = height ).pack()

sizes = tkinter.Label(text ="Sizes").pack()


reload = tkinter.Button(text="Reload- WIP", command=reload, bg = background, bd = border, width = width, height = height).pack()

window.mainloop()