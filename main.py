from tkinter import *


def convert():
    miles = float(input.get())
    km = miles * 1.609
    converted_label.config(text=km)



window = Tk()
window.minsize(width=300, height=200)
window.title('Miles to Kilometer Converter')
window.config(padx=50, pady=50)

equals_label = Label(text='is equal to')
equals_label.grid(column=0, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

miles_label = Label(text='miles')
miles_label.grid(column=2, row=0)

converted_label = Label(text='')
converted_label.grid(column=1, row=1)

km_label = Label(text='km')
km_label.grid(column=2, row=1)

button = Button(text='Calculate', command=convert)
button.grid(column=1, row=2)



window.mainloop()