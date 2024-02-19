from tkinter import *
demo=Tk()
demo.geometry("700x550")
demo.config(bg = '#d3f3f5')
demo.title("Student_Database")

def insert():
    a=str(invalue1.get())
    message.config(text=a)

name=Label(demo,text="Name",font="Arial 15 bold")

name.grid(row=0, column=20,padx=20,pady=20)

invalue1=Entry(demo,width=40)
invalue1.grid(row=0, column=25)


taml=Label(demo,text="Language1",font="Arial 15 bold")
taml.grid(row=1, column=20,padx=20, pady=20)

invalue2=Entry(demo,width=40)
invalue2.grid(row=1, column=25)



Engl=Label(demo,text="Language2",font="Arial 15 bold")
Engl.grid(row=2, column=20,padx=20, pady=20)

invalue3=Entry(demo,width=40)
invalue3.grid(row=2, column=25)


math=Label(demo,text="mathametics",font="Arial 15 bold")
math.grid(row=3, column=20,padx=20, pady=20)

invalue4=Entry(demo,width=40)
invalue4.grid(row=3, column=25)


sci=Label(demo,text="Science",font="Arial 15 bold")
sci.grid(row=4, column=20,padx=20, pady=20)

invalue5=Entry(demo,width=40)
invalue5.grid(row=4, column=25)



soci=Label(demo,text="Scocial science",font="Arial 15 bold")
soci.grid(row=5, column=20,padx=20, pady=20)

invalue6=Entry(demo,width=40)
invalue6.grid(row=5, column=25)

message=Entry(demo,width=50)
message.grid(row=1,column=90)



insert=Button(demo,text="INSERT",command=insert,font="Arial 11 ")
insert.grid(row=6, column=20)

update=Button(demo,text="UPDATE",font="Arial 11 ")
update.grid(row=6, column=22)

delete=Button(demo,text="DELETE",font="Arial 11 ")
delete.grid(row=7, column=20)

reset=Button(demo,text="RESET",font="Arial 11 ")
reset.grid(row=7,column=22)

submit=Button(demo,text="SUBMIT",font="Arial 11 ")
submit.grid(row=8, column=21)













demo.mainloop()
