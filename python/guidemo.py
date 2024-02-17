# from tkinter import *
# from tkinter import messagebox
# import random
# def no():
#     messagebox.showinfo(" ","Thank You!")
#     quit()
# def motionmouse(event):
#     btnYes.place(x=random.randint(0,500), y=random.randint(0,500))
# root =Tk()
# root.geometry("600x600")
# root.title("survey")
# root.resizable(width=False, height=False)
# root['bg']="yellow"
# lable=Label(root,text="Are you human?", font="Arial 20 bold",bg="yellow").pack()
# btnYes=Button(root,text="no",font="Arial 20 bold")
# btnYes.place(x=170,y=100)
# btnYes.bind("<Enter>",motionmouse)
# btnNo=Button(root,text="yes",font="Arial 20 bold",command=no).place(x=350,y=100)
# root.mainloop()

from tkinter import *
from tkinter import messagebox
user =Tk()
user.geometry("500x500")
user.title("LOGIN PAGE")

def no():
    a=str(entry1.get("saranya"))
    b=int(entry2.get(12345))
    messagebox.showinfo(" ","Login Succesfully Thank you!")
    quit()
    


    

message1=Label(user,text="Welcome To Login Page",font="Ariel 20 bold",fg="blue")
message1.grid(row=1, column=50,padx=80,pady=40)

message2=Label(user,text ="User Name")
message2.grid(row=4 ,column=50)

entry1=Entry(user,width=40)
entry1.grid(row=4, column=52, padx=80,pady=40)


message3=Label(user,text="Password")
message3.grid(row=5, column=50)


entry2=Entry(user,width=40)
entry2.grid(row=5, column=52,padx=80,pady=40)

btn=Button(user,text="login",command=no)
btn.grid(row=6, column=60)


user.mainloop()
