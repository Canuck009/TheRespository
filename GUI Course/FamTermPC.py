# 10:21 17 May 2022

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

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk, Image
import datetime
import pytz


##################################################
##################### Windows ####################

root = Tk()
root.configure(background = "#EDF3EE") # thats the colour for AC Nook Phone
root.title("Kennedy Family Terminal")
root.geometry("800x480")
root.iconbitmap('slo.ico')

##################### Windows ####################
##################################################
##################### Images #####################
sword = ImageTk.PhotoImage(Image.open("swordleaf180.png"))




##################### Images #####################
##################################################
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

################### Functions ####################
##################################################
################ Chore Check Page ################

def Chore_Win():
    global choreL
    choreL = Toplevel()
    choreL.configure(background = "#EDF3EE") # thats the colour for AC Nook Phone
    choreL.title("Kennedy Family Terminal")
    choreL.geometry("800x480")
    choreL.iconbitmap('slo.ico')
    chore_frame = Frame(choreL, height = 200, width = 780, bd = 10, relief = "raised")
    chore_frame.grid(row = 0, columnspan = 3)

    choreLab = Label(chore_frame, text = "Chores", relief = "groove", font = ("Arial", 70), state = "normal")
    choreLab.grid(row = 0, column = 1, padx = 15)

    homeIco = Label(chore_frame, image = sword)
    homeIco.grid(row = 0, column = 0)

    homeIco = Label(chore_frame, image = sword)
    homeIco.grid(row = 0, column = 2)

    # Chore Checkboxes

    BED_CHECK = Checkbutton(choreL, text = "Make Bed", variable = CT1, onvalue = 1.25, offvalue = 0.00, font = ("Arial", 20), width = 15, anchor = "w")
    BED_CHECK.deselect()
    BED_CHECK.grid(row = 1, column = 0)

    LAU_CHECK = Checkbutton(choreL, text = "Laundry Away", variable = CT2, onvalue = 1.25, offvalue = 0.00, font = ("Arial", 20), width = 15, anchor = "w")
    LAU_CHECK.deselect()
    LAU_CHECK.grid(row = 1, column = 1)

    LAUN_CHECK = Checkbutton(choreL, text = "Hamper", variable = CT3, onvalue = 0.25, offvalue = 0.00, font = ("Arial", 20), width = 15, anchor = "w")
    LAUN_CHECK.deselect()
    LAUN_CHECK.grid(row = 1, column = 2)

    TEETH1_CHECK = Checkbutton(choreL, text = "Brush Teeth AM", variable = CT4, onvalue = 0.75, offvalue = 0.00, font = ("Arial", 20), width = 15, anchor = "w")
    TEETH1_CHECK.deselect()
    TEETH1_CHECK.grid(row = 2, column = 0)

    TEETH2_CHECK = Checkbutton(choreL, text = "Brush Teeth PM", variable = CT5, onvalue = 0.75, offvalue = 0.00, font = ("Arial", 20), width = 15, anchor = "w")
    TEETH2_CHECK.deselect()
    TEETH2_CHECK.grid(row = 2, column = 1)

    DISH_CHECK = Checkbutton(choreL, text = "Dishes Away", variable = CT6, onvalue = 1.25, offvalue = 0.00, font = ("Arial", 20), width = 15, anchor = "w")
    DISH_CHECK.deselect()
    DISH_CHECK.grid(row = 2, column = 2)

    STABLE_CHECK = Checkbutton(choreL, text = "Set Table", variable = CT7, onvalue = 0.75, offvalue = 0.00, font = ("Arial", 20), width = 15, anchor = "w")
    STABLE_CHECK.deselect()
    STABLE_CHECK.grid(row = 3, column = 0)

    CTABLE_CHECK = Checkbutton(choreL, text = "Clear Table", variable = CT8, onvalue = 0.75, offvalue = 0.00, font = ("Arial", 20), width = 15, anchor = "w")
    CTABLE_CHECK.deselect()
    CTABLE_CHECK.grid(row = 3, column = 1)

    BEH_CHECK = Checkbutton(choreL, text = "Good Behaviour", variable = CT9, onvalue = 1.75, offvalue = 0.00, font = ("Arial", 20), width = 15, anchor = "w")
    BEH_CHECK.deselect()
    BEH_CHECK.grid(row = 3, column = 2)

    Totbut = Button(choreL, text = "Total", command = totaL, font = ("Arial", 20), width = 15)
    Totbut.grid(row = 4, column = 0)

    chore_quit = Button(choreL, text = "Quit", command = choreL.destroy, font = ("Arial", 20), width = 15)
    chore_quit.grid(row = 4, column = 2)

    choreL.mainloop()

def totaL():
    TotaL00 = float(CT1.get()) + float(CT2.get()) + float(CT3.get()) + float(CT4.get()) + float(CT5.get()) + float(CT6.get()) + float(CT7.get()) + float(CT8.get()) + float(CT9.get())
    TotaL = "{:.2f}".format(TotaL00)
    TotLab = Label(choreL, text = f"£ {TotaL}", font = ("Arial", 20), width = 10, relief = "sunken")
    TotLab.grid(row = 4, column = 1, )
    

################ Chore Check Page ################
##################################################
################### Calander #####################

def calen():

    fcal = Toplevel()
    fcal.geometry("800x480")
    fcal.configure(background = "#EDF3EE") # thats the colour for AC Nook Phone
    fcal.title("Kennedy Family Calander")
    fcal.geometry("800x480")
    fcal.iconbitmap('slo.ico')
    cal = Calendar(fcal, selectmode = "none")
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, "Alyxis' School Play", "message")
    cal.calevent_create(date, "Meeting Reminder", "reminder")
    cal.calevent_create(date + cal.timedelta(days=-2), "Holiday", "reminder")
    cal.calevent_create(date + cal.timedelta(days=3), "Business Trip", "message")
    cal.pack(fill="both", expand=True)

    cal_quit = Button(fcal, text = "Quit", command = fcal.destroy, font = ("Arial", 20), width = 15)
    cal_quit.pack()

    fcal.mainloop()


################### Calander #####################
##################################################
################### Variables ####################

CT1 = StringVar()
CT2 = StringVar()
CT3 = StringVar()
CT4 = StringVar()
CT5 = StringVar()
CT6 = StringVar()
CT7 = StringVar()
CT8 = StringVar()
CT9 = StringVar()



################### Variables ####################
##################################################
##################### Script #####################
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

A_chore = Button(root, text = "Alyxis' Chores", command = Chore_Win, font = ("Arial", 20), width = 15)
A_chore.grid(row = 4, column = 2)

T_chore = Button(root, text = "Thomas' Chores", command = Chore_Win, font = ("Arial", 20), width = 15)
T_chore.grid(row = 5, column = 2, pady = 5)

Q_click = Button(root, text = "Quit", command = root.quit, font = ("Arial", 20), width = 15)
Q_click.grid(row = 6)

cal_clik = Button(root, text = "Calendar", font = ("Arial", 20), width = 15, command = calen)
cal_clik.grid(row = 1, column = 2)

Menu_clik = Button(root, text = "Meal Plan", font = ("Arial", 20), width = 15)
Menu_clik.grid(row = 1, column = 1)





##################### Script #####################
##################################################






root.mainloop()
