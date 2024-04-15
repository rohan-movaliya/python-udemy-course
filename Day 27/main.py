# MILES TO KILOMETER CONVERTER

import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)


# ------------MILE_INPUT------------
mile_input = tkinter.Entry(width=10)
mile_input.grid(column=1, row=0)


# ------------MILE_LABLE------------
mile_lable = tkinter.Label(text="Miles")
mile_lable.grid(column=2, row=0)


# ------------IS_EQUAL_TO_LABLE------------
is_equal_to_lable = tkinter.Label(text="is equal to")
is_equal_to_lable.grid(column=0, row=1)


# ------------KM_OUTPUT------------
km_output = tkinter.Label(text="0")
km_output.grid(column=1, row=1)


# ------------KM_LABLE------------
km_lable = tkinter.Label(text="Km")
km_lable.grid(column=2, row=1)


# ------------CALCULATE_BUTTON------------
def action_calculate():
    miles = float(mile_input.get())
    km = round(miles * 1.609, 2)
    km_output.config(text=km)


button = tkinter.Button(text="Calculate", command=action_calculate)
button.grid(column=1, row=2)


window.mainloop()
