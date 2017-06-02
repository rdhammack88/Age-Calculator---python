import tkinter
from tkinter import *
from tkinter import ttk

def age_calc():
    user_choice = users_choice.get()
    user_age = int(users_age.get())
    if user_choice == '1':
        months = user_age * 12
        age = "Your age in months is {}".format(months)
    elif user_choice == '2':
        weeks = user_age * 52
        age = "Your age in weeks is {}".format(weeks)
    elif user_choice == '3':
        days = user_age * 365
        age = "Your age in days is {}".format(days)
    elif user_choice == '4':
        hours = user_age * 365 * 24
        age = "Your age in hours is {}".format(hours)
    elif user_choice == '5':
        minute = user_age * 365 * 24 * 60
        age = "Your age in minutes is {}".format(minute)
    elif user_choice == '6':
        seconds = user_age * 365 * 24 * 60 * 60
        age = "Your age in seconds is {}".format(seconds)
    else:
        age = "That's not a valid choice"
    results.delete(0.0, END)
    results.insert(0.0, age)

instructions = "Tell me what your age is and I'll translate it into months, weeks, days, hours, minutes, or seconds, depending on your choice."
choices = " 1. Months\n 2. Weeks\n 3. Days\n 4. Hours\n 5. Minutes\n 6. Seconds"


root = tkinter.Tk()
root.title("Age Calculator")
root.geometry("1000x700")
frame_1 = Frame()
frame_1.pack()

    # create the widgets to appear
instr = Text(frame_1, width=40, height=7, wrap=WORD)
instr.pack(side = LEFT)
instr.delete(0.0, END)
instr.insert(0.0, instructions)
choice = Text(frame_1, width=40, height=7, wrap=WORD)
choice.pack(side = RIGHT)
choice.delete(0.0, END)
choice.insert(0.0, choices)

# user entered widgets
age_lbl = ttk.Label(root, text="How old are you?")
age_lbl.pack()
users_age = ttk.Entry(root)
users_age.pack()
choice_lbl = Label(root, text="How would you like to calculate your age?")
choice_lbl.pack()
users_choice = Entry(root)
users_choice.pack()

# calculate age results widget
generate_btn = ttk.Button(root, text = "Calculate your age!", command = age_calc)
generate_btn.place(x = 200, y = 500)

# display results widget
results = Text(root, width=50, height=5, wrap=WORD)
results.place(x = 200, y = 400)

root.mainloop()
