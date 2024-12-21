from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=200)
window.config(padx=20, pady=20)

input = Entry()
input.grid(row=0, column=1)

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

result = Label(text="0")
result.grid(row=1, column=1)

label3 = Label(text="Km")
label3.grid(row=1, column=2)


def calculate():
    dist_mile = int(input.get())
    dist_km = dist_mile * 1.6
    result.config(text=f"{dist_km}")


btn = Button(text="Calculate", command=calculate)
btn.grid(row=2, column=1)


window.mainloop()
