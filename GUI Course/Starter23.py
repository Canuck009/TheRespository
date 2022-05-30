# 11:40 23 Apr 2022

# Using Git Bash - file directories a "\" has to be placed before spaces.
# cd OneDrive\ -\ University\ of\ Brighton/~~\ Yr4\ Masters/XE703\ -\ Independant\ Study/GUIs

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

# Popup window types
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.configure(background = "#EDF3EE") # thats the colour for AC Nook Phone
root.title("Kennedy Family Terminal")
root.geometry("800x480")
root.iconbitmap('sl.ico')

###################### ADMIN #####################
##################################################
##################### Images #####################
sword = ImageTk.PhotoImage(Image.open("swordleaf180.png"))




##################### Images #####################
##################################################
################### Functions ####################

def popup():
    messagebox.askquestion("Popup Tittle", "Look FFS!!!!")








################### Functions ####################
##################################################
################### Variables ####################










################### Variables ####################
##################################################
##################### Script #####################

pop_button = Button(root, text = "Click to Pop-Up", command = popup)
pop_button.pack(pady = 20)








root.mainloop()
