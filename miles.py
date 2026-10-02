from tkinter import*
import tkinter as tk
window= Tk() 
window.title("distance converter")
window.geometry("300x100")
l1= Label(window,text="Enter miles:")
l2= Label(window,text="Kilometers")
def convert():
    number= enter.get()
    km= float(number)* 1.609
    t1.delete("1.0",END)
    t1.insert(END,km)
button= Button(window,text="Convert",command= convert)
enter= Entry(window)
t1= Text(window,height=1,width=20)
l1.grid(row=0,column=0)
enter.grid(row=0,column=1)
button.grid(row=0,column=2)
l2.grid(row=1,column=0)
t1.grid(row=2,column=1)
window.mainloop()