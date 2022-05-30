# 15:29 19Apr 2022

# Using Git Bash - file directories a "\" has to be placed before spaces.
# cd c:/Users/Seank/OneDrive\ -\ University\ of\ Brighton/~~\ Yr4\ Masters/XE703\ -\ Independant\ Study/GUIs

# Its also good practice to create a virtual environment in the directory that youre using so that not to alter and damage other things in your actual computer. "python -m venv virt" is the command to make one.

# -> python (stating the kind of virtual environment wanted)
# -> -m (called a "command option")
# -> venv (means virtual environment)
# -> virt (is just what i called it, can be called anything)

## To run
# python [name of program.py]

## To activate the virtual environment...
# source virt/Scripts/activate (note the capital S)
## To Deactivate ....
# deactivate

# Using Pillow.... Couldnt install into VEnv ... googled to death, and this worked...
# python -m pip install -U --force-reinstall pip

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.configure(background = "#EDF3EE") # thats the colour for AC Nook Phone
root.title("Kennedy Family Terminal")
root.geometry("800x480")
root.iconbitmap('sl.ico')

##################### Images ##########################

sword = ImageTk.PhotoImage(Image.open("swordleaf180.png"))


##################### Images ##########################

def clicked(): # a function needed to be defined so that we could use it later in the code.
    global confirm_label1
    confirm_label1 = Label(root, text = "Welcome Parent") # this will display when its clicked.
    confirm_label1.grid(row = 1, column = 1)

def hide():
    confirm_label1.grid_forget()

def show():
    confirm_label1.grid(row = 1, column = 1)

def destro_y():
    confirm_label1.destroy()

homeLab = Label(root, text = "Home", relief = "groove", font = ("Arial", 80), state = "normal")
homeLab.grid(row = 0, column = 1)

homeIco = Label(root, image = sword)
homeIco.grid(row = 0, column = 0)

parent_clik = Button(root, text = "Parent",command = clicked, relief = "groove", font = ("Arial", 30), state = "normal")
parent_clik.grid(row = 1, pady = 3)

T_click = Button(root, text = "hide button", command = hide)
T_click.grid(row = 4)

A_click = Button(root, text = "Show button", command = show)
A_click.grid(row = 5)

D_click = Button(root, text = "Destroy button", command = destro_y)
D_click.grid(row = 6)


















root.mainloop()
