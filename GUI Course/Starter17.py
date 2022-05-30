# 10:21 21 Apr 2022

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

root = Tk()
root.configure(background = "#EDF3EE") # thats the colour for AC Nook Phone
root.title("Kennedy Family Terminal")
root.geometry("800x480")
root.iconbitmap('sl.ico')

##################### Images #####################

sword = ImageTk.PhotoImage(Image.open("swordleaf180.png"))


##################### Images #####################

################### Functions ####################

def clicked(): # a function needed to be defined so that we could use it later in the code.
    pass
    # global confirm_label1
    # confirm_label1 = Label(root, text = "Welcome Parent") # this will display when its clicked.
    # confirm_label1.grid(row = 1, column = 1)


def A_Balance():
    global A_bal
    A_bal = Label(root, text = "Account Balance: £12.75 ", font = ("Arial", 12), bd = 5) #function for allowance calc.
    A_bal.grid(row = 4, column = 1)

def T_Balance():
    global T_bal
    T_bal = Label(root, text = "Account Balance: £13.50 ", font = ("Arial", 12)) #function for allowance calc.
    T_bal.grid(row = 5, column = 1)

def A_Chore_Menu():
    pass

def T_Chore_Menu():
    pass


################### Functions ####################

head_frame = Frame(root, height = 200, width = 780, bd = 10, relief = "raised")
head_frame.grid(row = 0, columnspan = 3, padx = 15, pady = 10)

homeLab = Label(head_frame, text = "Home", relief = "groove", font = ("Arial", 80), state = "normal")
homeLab.grid(row = 0, column = 1, padx = 40)

homeIco = Label(head_frame, image = sword)
homeIco.grid(row = 0, column = 0)

homeIco = Label(head_frame, image = sword)
homeIco.grid(row = 0, column = 2)

parent_clik = Button(root, text = "Parent",command = clicked, font = ("Arial", 20), state = "normal", width = 15)
parent_clik.grid(row = 1, pady = 5)

A_click = Button(root, text = "Alyxis", command = A_Balance, font = ("Arial", 20), width = 15)
A_click.grid(row = 4,)

T_click = Button(root, text = "Thomas", command = T_Balance, font = ("Arial", 20), width = 15)
T_click.grid(row = 5, pady = 5)

A_chore = Button(root, text = "Alyxis' Chores", command = A_Chore_Menu, font = ("Arial", 20), width = 15)
A_chore.grid(row = 4, column = 2)

T_chore = Button(root, text = "Thomas' Chores", command = T_Chore_Menu, font = ("Arial", 20), width = 15)
T_chore.grid(row = 5, column = 2, pady = 5)

Q_click = Button(root, text = "Quit", command = root.quit, font = ("Arial", 20), width = 15)
Q_click.grid(row = 6)

cal_clik = Button(root, text = "Calendar", font = ("Arial", 20), width = 15)
cal_clik.grid(row = 1, column = 2)

Menu_clik = Button(root, text = "Meal Plan", font = ("Arial", 20), width = 15)
Menu_clik.grid(row = 1, column = 1)







root.mainloop()
