

from tkinter import *
from tkinter import messagebox
import mysql.connector

win=Tk()

win.title("Insert into MYSQL DB Demo")
win.geometry("500x500")

class sqlconnection:
    def __init__(self):
        
        dbcon=mysql.connector.connect(
        host="192.168.1.240",
        user="AIBATCH01",
        password="AI@123",
        database="ai_saranya"
        )
        return dbcon

    
    def add(self):
        value=self.invalue.get()
        value1=self.invaluen.get()
        e_con=self.MyDBConnection()
        result=e_con.cursor()
        statement="insert into demo (reg_no,name) values (%s,%s);"
        valuepass=(value,value1)
        result.execute(statement,valuepass)
        e_con.commit()
        print(messagebox.showinfo("","Inserted succesfully"))
        quit()
    def update(self):
        print(messagebox.showinfo("","Updated succesfully"))
        quit()
    
    def delete(self):
        print(messagebox.showinfo("","Deleted succesfully"))
        quit()
   
    

  

        


class frameDBoperations(sqlconnection):
    def __init__(self) :
        
        frametop=Frame(win,bg="blue",width=500,height=500, padx=30,pady=30)
        frametop.pack(side = TOP)
        btninsert=Button(frametop,text="INSERT",command=self.frameleft).pack(padx=10,pady=10)
        btnupdate=Button(frametop,text="UPDATE",command=self.frameright).pack(padx=10,pady=10)
        btndelete=Button(frametop,text="DELETE",command=self.framebottom).pack(padx=10,pady=10)

    
    def frameleft(self):
        new=Tk()
        new.title("STUDENT DATABASE")

        frameleft=Frame(new,bg="yellow",width=500,height=500, padx=30,pady=30)
        frameleft.pack(side = LEFT)
        # super().__init_(self,invalue,invaluen)

        lbl_Title_of_oeration=Label(frameleft,text="Insert into MYSQL DB Demo")
        lbl_Title_of_oeration.grid(row=0, columnspan=5)

        lblname=Label(frameleft,text="REG.NO")
        lblname.grid(row=2, column=1,padx=30,pady=10)

        invalue=Entry(frameleft,width=30)
        invalue.grid(row=2, column=3)

        lblTamil=Label(frameleft,text="NAME")
        lblTamil.grid(row=3, column=1,padx=30,pady=10)

        invaluen=Entry(frameleft,width=30)
        invaluen.grid(row=3, column=3)

        submit=Button(frameleft,text="INSERT",command=self.add)
        submit.grid(row=4, column=3)

        

    def frameright(self):

        newW=Tk()
        newW.title("STUDENT DATABASE")

        frameright=Frame(newW,bg="red",width=500,height=500,padx=30,pady=30)
        frameright.pack(side = RIGHT)

        lbl_Title_of_oeration=Label(frameright,text="Update into MYSQL DB Demo")
        lbl_Title_of_oeration.grid(row=0, columnspan=5)

        lblname=Label(frameright,text="REG.NO")
        lblname.grid(row=2, column=1,padx=30,pady=10)

        invalue1=Entry(frameright,width=30)
        invalue1.grid(row=2, column=3)


        lblTamil=Label(frameright,text="NAME")
        lblTamil.grid(row=3, column=1,padx=30,pady=10)

        invalue2=Entry(frameright,width=30)
        invalue2.grid(row=3, column=3)

        update=Button(frameright,text="UPDATE",command=self.update)
        update.grid(row=4, column=3)



    def framebottom(self):

        newW=Tk()
        newW.title("STUDENT DATABASE")

        framebottom=Frame(newW,bg="green",width=300,height=300,padx=30,pady=30)
        framebottom.pack(side= BOTTOM)

        lbl_Title_of_oeration=Label(framebottom,text="delete into MYSQL DB Demo")
        lbl_Title_of_oeration.grid(row=0, columnspan=5)

        lblname=Label(framebottom,text="REG-NO")
        lblname.grid(row=2, column=1,padx=30,pady=10)

        invalue1=Entry(framebottom,width=30)
        invalue1.grid(row=2, column=3)


        lblTamil=Label(framebottom,text="NAME")
        lblTamil.grid(row=3, column=1,padx=30,pady=10)

        invalue2=Entry(framebottom,width=30)
        invalue2.grid(row=3, column=3)

        delete=Button(framebottom,text="DELETE",command=self.delete)
        delete.grid(row=4, column=3)



run=frameDBoperations()
win.mainloop()
