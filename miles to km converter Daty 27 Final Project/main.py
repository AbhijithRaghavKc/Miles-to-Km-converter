from tkinter import *

window = Tk()
window.title("Miles To KM Converter")
# window.minsize(width=500,height=300)
window.config(padx=20,pady=20)


def button_click():

    mile = float(input_mile.get())
    to_km = round(mile * 1.60934)
    my_label_km_converted.config(text=f"{to_km}")


input_mile = Entry(width=10)
input_mile.grid(column=1,row=0)

my_label_miles = Label(text="Miles")
my_label_miles.grid(column=3, row=0)

my_label_equal_to = Label(text="is equal to")
my_label_equal_to.grid(column=0, row=1)


my_label_km_converted = Label(text="0")
my_label_km_converted.grid(column=1, row=1)

my_label_km = Label(text="KM")
my_label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_click)
button.grid(column=1,row=2)







window.mainloop()
