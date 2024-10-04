from tkinter import *
from tkinter import messagebox
import random

window=Tk()

#...................................................WORKING............................................................
def save():

    website=i1.get()
    email=i2.get()
    password=i3.get()

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="OOPS",message="Make sure you don't leave any information unfilled.")
    else:
        is_okay=messagebox.askokcancel(title=website,message=f"These are the information entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save it?")

        if is_okay:
            with open("data.txt","a") as data_file:
                data_file.write(f"\n{website} | {email} | {password}")
                i1.delete(0,END)
                i3.delete(0,END)


window.title("Password Generator")
#window.minsize(width=550,height=400)
canvas=Canvas(width=200,height=200)
image2=PhotoImage(file="logo.png")
window.config(padx=50,pady=50)
canvas.create_image(100,100,image=image2)
canvas.grid(row=0,column=1)

l1=Label(text="Website:",font=("Arial",11,"normal"))
l1.grid(row=1,column=0)
i1=Entry(width=35)
i1.grid(row=1,column=1,columnspan=2)
i1.focus()

l2=Label(text="Email/Username: ",font=("Arial",11,"normal"))
l2.grid(row=2,column=0)
i2=Entry(width=35)
i2.grid(row=2,column=1,columnspan=2)
i2.insert(END,"manish12345g@gmail.com")

l3=Label(text="Password:",font=("Arial",11,"normal"))
l3.grid(row=3,column=0)
i3=Entry(width=17)
i3.grid(row=3,column=1)

b1=Button(text="Generate Password")
b1.grid(row=3,column=2)
b2=Button(text="Add",width=30,command=save)
b2.grid(row=4,column=1,columnspan=2)





window.mainloop()