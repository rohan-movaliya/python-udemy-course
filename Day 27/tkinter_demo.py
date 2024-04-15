from tkinter import *

window = Tk()
window.title("Tkinter Demo")
# window.minsize(width=500, height=500)
# window.config(padx=100,pady=200)


# --------------LABLE--------------
my_lable = Label(text="I am Rohan", font=("Arial", 24, "italic"))
my_lable.config(text="Rohan Movaliya")
# POSITIONING
# my_lable.pack(side="left")
# my_lable.place(x=0, y=0)
# my_lable.grid(row=0, column=0)
my_lable.pack()
my_lable.config(padx=50, pady=50)


# --------------BUTTON--------------
def action_button_clicked_me():
    # print("Button was clicked")
    my_lable.config(text=input.get())


button = Button(text="Click Me", command=action_button_clicked_me)
# button.grid(row=1, column=1)
button.pack()

new_button = Button(text="Click Again", command=action_button_clicked_me)
# new_button.grid(row=0, column=2)
new_button.pack()


# --------------ENTRY--------------
input = Entry(width=10)
# add some text to begin with
input.insert(END, string="Write anything.")
# gets text in entry
print(input.get())
# input.grid(row=2, column=3)
input.pack()


# # --------------TEXTBOX--------------
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
# text.grid(row=4, column=0)
text.pack()


# # --------------SPINBOX--------------
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# #--------------SCALE--------------
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# #--------------CHECKBUTTON--------------
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used
)
checked_state.get()
checkbutton.pack()


# #--------------RADIOBUTTON--------------
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(
    text="Option1", value=1, variable=radio_state, command=radio_used
)
radiobutton2 = Radiobutton(
    text="Option2", value=2, variable=radio_state, command=radio_used
)
radiobutton1.pack()
radiobutton2.pack()


# #--------------LISTBOX--------------
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
