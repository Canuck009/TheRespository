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

from tkinter import *
from PIL import ImageTk, Image


choreL = Toplevel()
choreL.configure(background = "#EDF3EE") # thats the colour for AC Nook Phone
choreL.title("Kennedy Family Terminal")
choreL.geometry("800x480")
choreL.iconbitmap('sl.ico')

###################### ADMIN #####################
##################################################
##################### Images #####################
sword = ImageTk.PhotoImage(Image.open("swordleaf180.png"))




##################### Images #####################
##################################################
################### Functions ####################

def totaL():
    TotLab = Label(choreL, text = "£ " + CT1.get(float()) + CT2.get() + CT3.get(), font = ("Arial", 20), width = 15)
    TotLab.grid(row = 4, column = 1, columnspan = 3)





################### Functions ####################
##################################################
################### Variables ####################
CT1 = StringVar()
CT2 = StringVar()
CT3 = StringVar()



################### Variables ####################
##################################################
##################### Script #####################

chore_frame = Frame(choreL, height = 200, width = 780, bd = 10, relief = "raised")
chore_frame.grid(row = 0, columnspan = 3, padx = 20, pady = 10)

choreLab = Label(chore_frame, text = "Chores", relief = "groove", font = ("Arial", 70), state = "normal")
choreLab.grid(row = 0, column = 1, padx = 40)

homeIco = Label(chore_frame, image = sword)
homeIco.grid(row = 0, column = 0)

homeIco = Label(chore_frame, image = sword)
homeIco.grid(row = 0, column = 2)


# Checkboxes

BED_CHECK = Checkbutton(choreL, text = "Make Bed", variable = CT1, onvalue = 1.50, offvalue = 0.00, font = ("Arial", 20), width = 15)
BED_CHECK.deselect()
BED_CHECK.grid(row = 1, column = 0)

LAU_CHECK = Checkbutton(choreL, text = "Laundry Away", variable = CT2, onvalue = 1.50, offvalue = 0.00, font = ("Arial", 20), width = 15)
LAU_CHECK.deselect()
LAU_CHECK.grid(row = 1, column = 1)

LAUN_CHECK = Checkbutton(choreL, text = "Hamper", variable = CT3, onvalue = 0.50, offvalue = 0.00, font = ("Arial", 20), width = 15)
LAUN_CHECK.deselect()
LAUN_CHECK.grid(row = 1, column = 2)


Totbut = Button(choreL, text = "Total", command = totaL, font = ("Arial", 20), width = 15)
Totbut.grid(row = 3, column = 1, columnspan = 3)










choreL.mainloop()
