# 14:29 19Apr 2022


# Using Git Bash - file directories a "\" has to be placed before spaces.
# cd c:/Users/Seank/OneDrive\ -\ University\ of\ Brighton/~~\ Yr4\ Masters/XE703\ -\ Independant\ Study/GUIs/

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

from tkinter import *

root = Tk()
root.configure(background = "#EDF3EE") # thats the colour for AC Nook Phone
root.title("Kennedy Family Terminal")
root.geometry("800x480")
root.iconbitmap("c:/Users/Seank/OneDrive - University of Brighton/~~ Yr4 Masters/XE703 - Independant Study/GUIs/Media/slo.ico") # Adds a little icon to the top of the window.**not that the address for file locations DOESNT need the \ around the spaces.


# # homelab0 = Label(root, text = ("HOME"), relief = "groove", font = ("Arial", 40), state = "normal")
# # homelab0.grid(row = 0, column = 0, columnspan = 2)

# # homelab2 = Label(root, text = ("Parent"), relief = "groove", font = ("Arial", 32), state = "normal")
# # homelab2.grid(row = 1, column = 0, sticky = W)

# # homelab3 = Label(root, text = ("Alyxis"), relief = "groove", font = ("Arial", 32), state = "normal")
# # homelab3.grid(row = 2, column = 0, sticky = W)

# # homelab4 = Label(root, text = ("Thomas"), relief = "groove", font = ("Arial", 32), state = "normal")
# # homelab4.grid(row = 2, column = 1, sticky = W)

# # for grid, sticky can be used with cardnial directions to justify text.
# # there is also rowspan and columnspan which centres the widget between those columns/rows.

# Making buttons!!! just like label widgets EXACTLY! except we can create a "clicked" function to do somthing else.

def clicked(): # a function needed to be defined so that we could use it later in the code.
    confirm_label1 = Label(root, text = "Are You Sure?") # this will display when its clicked.
    confirm_label1.grid(row = 2)

def clicked2(): # a function needed to be defined so that we could use it later in the code.
    confirm_label2 = Label(root, text = "Hello " + ent_wig2.get()) # this will display when its clicked.
    confirm_label2.grid(row = 6)

home_button = Button(root, text = "Home",command = clicked, relief = "groove", font = ("Arial", 40), state = "normal")
home_button.grid(row = 0)

# Entry Widget - an input box
entr_wig = Entry(root, text = "Name?", width = 30)
entr_wig.grid(pady = 3)

name_button = Button(root, text = "Enter Your Name",command = clicked2, relief = "groove", font = ("Arial", 40), state = "normal")
name_button.grid(row = 4)

# Entry Widget - an input box
ent_wig2 = Entry(root, text = "Name?", width = 30)
ent_wig2.grid(pady = 5, row = 5)




root.mainloop()
