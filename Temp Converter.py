from tkinter import *

window = Tk()
window.title("Temp Converter")
window.geometry("300x300")


def convert_tem():
    if e2.get() == "":
        temp = float(e1.get())
        e2.insert(0, round(9*temp/5+32,2))
        if float(e1.get())>28:
            l4 = Label(window, text="It is very hot! Make sure to bring water with you!") 
        elif 28>=float(e1.get())>18:
            l4 = Label(window, text="What a nice weather. Enjoy your day!") 
        elif 18>=float(e1.get())>8:
            l4 = Label(window, text="It's cool outside! Keep yourself warm not to catch a cold")
        elif 8>float(e1.get()):
            l4 = Label(window, text="Be prepared for cold weather. Wear a warm clothes")
        return l4.grid(row=4, columnspan=4)
    else:
        temp = float(e2.get())
        e1.insert(0, round((temp-32)*5/9,2))
        if float(e1.get())>28:
            l4 = Label(window, text="It is very hot! Make sure to bring water with you!")
        elif 28>=float(e1.get())>18:
            l4 = Label(window, text="What a nice weather. Enjoy your day!")
        elif 18>=float(e1.get())>8:
            l4 = Label(window, text="It's cool outside! Keep yourself warm not to catch a cold")
        elif 8>float(e1.get()):
            l4 = Label(window, text="Be prepared for cold weather. Wear a warm clothes")
        return l4.grid(row=4, columnspan=4)


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    
    


l1 = Label(window, text="C")
l2 = Label(window, text="F")
l3 = Label(window, height=1)
l4 = Label(window, text="")
l1.grid(row=0, column=0)
l2.grid(row=0, column=3)
l3.grid(row=2)
l4.grid(row=4, columnspan=4)


e1=Entry(window)
e2=Entry(window)
e1.grid(row=1, column=0)
e2.grid(row=1, column=3)

b1=Button(window, text="Convet", width=11, height=2, command=convert_tem)
b1.grid(row=3, columnspan=2)    
b2=Button(window, text="Clear", width=11, height=2, command=clear)
b2.grid(row=3, column=3, columnspan=2)

window.mainloop()
