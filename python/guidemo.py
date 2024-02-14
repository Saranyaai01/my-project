from tkinter import *
from tkinter import messagebox
import random
def no():
    messagebox.showinfo(" ","Thank You!")
    quit()
def motionmouse(event):
    btnYes.place(x=random.randint(0,500), y=random.randint(0,500))
root =Tk()
root.geometry("600x600")
root.title("survey")
root.resizable(width=False, height=False)
root['bg']="yellow"
lable=Label(root,text="Are you human?", font="Arial 20 bold",bg="yellow").pack()
btnYes=Button(root,text="no",font="Arial 20 bold")
btnYes.place(x=170,y=100)
btnYes.bind("<Enter>",motionmouse)
btnNo=Button(root,text="yes",font="Arial 20 bold",command=no).place(x=350,y=100)
root.mainloop()

