import tkinter
from tkinter import *

def button_clicked():
    num=int(input.get())
    num=num*1.6
    sec_label.config(text=f"is equal to   {num}")

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=350,height=200)

my_label=tkinter.Label(text="Miles")
my_label.place(x=190,y=50)

sec_label=tkinter.Label(text="is equal to ")
sec_label.place(x=50,y=70)

third_label=tkinter.Label(text="Km")
third_label.place(x=190,y=70)


input=Entry(width=10)
input.insert(END,string="0")
input.place(x=120,y=50)

button=Button(text="Calculate",command=button_clicked)
button.place(x=120,y=90)

















window.mainloop()