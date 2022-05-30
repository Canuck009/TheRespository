# 13:39 19 April 2022

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

# TKinter start! (the * means import everything)
from tkinter import *

# we want this to always be running and being refered to, so it needs to be a loop (always checking what to do). That is done with this Root command (Note Tk -> T capital, k Small) at the top of our script and root.mainloop() and the very end of the script.
root = Tk()

# Lets choose a colour for the main page.
root.configure(background = "#EDF3EE") # thats the colour for AC Nook Phone

# Lets write a Title
root.title("Kennedy Family Terminal")

# The window size can be added here too
root.geometry("800x480")


# TKinter is made primarily of widgets.
# You Create a widget
# You put it on your screen.

#homelab = Label(root, text = ("Home"), relief = "groove", font = ("Arial", 32), state = "normal")
#homelab.pack()

# The above example named our variable, called homelab and in the variable is a Lable.
# Lable([location], [Contents])
# Below that we are placing it on out "root" screen with the "pack" method which is exactly what it sounds like. its just packed onto the screen wherever it will fit.

# Playing with labels -
# the text colour (fg) and backround (bg) can be changed - DOES NOT EFFECT THE MAIN SCREEN COLOUR.
# font can be added "font = ("Arial"), SIZE).
# relief - either raised, sunken, groove, ridge.
# state - disabled, normal(great for buttons that need other conditions to be met to be clicked. )
# height - in pxl eg. 200. (doesnt make text bigger, only text box)
# width - in pxl eg. 200. (doesnt make text bigger, only text box)

#homelab1 = Label(root, text = ("Choose Your Option"), fg = "white", bg = "blue", font = ("Arial", 16), relief = "ridge", state = "disabled")
#homelab1.pack(pady = 50)
# Playing with Pack
# pad[] - x or y to give "padding" around it in relation to other objects.

# Grid System (cannot be used at the same time as pack)

homelab0 = Label(root, text = ("HOME"), relief = "groove", font = ("Arial", 40), state = "normal")
homelab0.grid(row = 0, column = 0, columnspan = 2)

homelab2 = Label(root, text = ("Parent"), relief = "groove", font = ("Arial", 32), state = "normal")
homelab2.grid(row = 1, column = 0, sticky = W)

homelab3 = Label(root, text = ("Alyxis"), relief = "groove", font = ("Arial", 32), state = "normal")
homelab3.grid(row = 2, column = 0, sticky = W)

homelab4 = Label(root, text = ("Thomas"), relief = "groove", font = ("Arial", 32), state = "normal")
homelab4.grid(row = 2, column = 1, sticky = W)

# for grid, sticky can be used with cardnial directions to justify text.
# there is also rowspan and columnspan which centres the widget between those columns/rows.

photo_image = PhotoImage(file = 'Menu_Map_NH_Icon.png')



root.mainloop()
