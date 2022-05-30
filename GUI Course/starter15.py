# 21:55 20 Apr 2022

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

##################### Images #####################

sword = ImageTk.PhotoImage(Image.open("swordleaf180.png"))


##################### Images #####################

################### Functions ####################

def fake_command():
    pass



################### Functions ####################


# Define menu!  pretty much just creates rthe menu BAR. There are no subjects, like "file, edit..." etc.
menu1 = Menu(root)
root.config(menu = menu1)


# Create menu items (the file, edit etc. )
file_menu = Menu(menu1) # so the menu command says youre making a menu, and then WHERE the menu is.
menu1.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = fake_command)
file_menu.add_separator()
file_menu.add_command(label = "Quit", command = root.quit)

edit_menu = Menu(menu1) # so the menu command says youre making a menu, and then WHERE the menu is.
menu1.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command = fake_command)
edit_menu.add_separator()
edit_menu.add_command(label = "Quit", command = root.quit)











root.mainloop()
