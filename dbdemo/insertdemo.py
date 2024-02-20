from tkinter import *
import mysql.connector
win=Tk()

win.title("Insert into MYSQL DB Demo")
win.geometry("500x500")

class frameDBoperations:
    def __init__(self) :
        frametop=Frame(win,bg="blue",width=500,height=500, padx=30,pady=30)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT",command=self.frameLeft).pack(padx=10,pady=10)
        btnupdate=Button(frametop,text="UPDATE",command=self.frameright).pack(padx=10,pady=10)
        btndelete=Button(frametop,text="DELETE").pack(padx=10,pady=10)
   
   
    def frameLeft(self):
        
        frameleft=Frame(win,bg="blue",width=300,height=300, padx=30,pady=30)
        frameleft.pack(side = LEFT)

        # frameright=Frame(win,bg="red",width=300,height=300)
        # frameright.pack(side = RIGHT)

        lbl_Title_of_oeration=Label(frameleft,text="Insert into MYSQL DB Demo")
        lbl_Title_of_oeration.grid(row=0, columnspan=5)

        lblname=Label(frameleft,text="Name")
        lblname.grid(row=2, column=1,padx=30,pady=10)

        lblTamil=Label(frameleft,text="Tamil")
        lblTamil.grid(row=3, column=1,padx=30,pady=10)

    def frameright(self):

        newW=Tk()
        newW.title("Update into MYSQL DB Demo")

        frameright=Frame(newW,bg="red",width=300,height=300)
        frameright.pack(side = RIGHT)

        lbl_Title_of_oeration=Label(frameright,text="Insert into MYSQL DB Demo")
        lbl_Title_of_oeration.grid(row=0, columnspan=5)

        lblname=Label(frameright,text="Name")
        lblname.grid(row=2, column=1,padx=30,pady=10)

        lblTamil=Label(frameright,text="Tamil")
        lblTamil.grid(row=3, column=1,padx=30,pady=10)



run=frameDBoperations()

win.mainloop()
