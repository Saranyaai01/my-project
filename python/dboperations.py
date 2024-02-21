from tkinter import *
from tkinter import messagebox
import mysql.connector
demo=Tk()
demo.geometry("800x600+300+60")
demo.config(bg = '#d3f3f5')
demo.title("Student_Database")

def MyDBConnection():
    dbcon=mysql.connector.connect(
    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_saranya"
    )
    return dbcon

def insertvalues():
    value=invalue.get()
    value1=invalue1.get()
    value2=invalue2.get()
    value3=invalue3.get()
    value4=invalue4.get()
    value5=invalue5.get()
    value6=invalue6.get()
    establishcon=MyDBConnection()
    result=establishcon.cursor()

    statement="insert into student_database(ID,name,language1,language2,mathematics,science,socialscience) values (%s,%s,%s,%s,%s,%s,%s);"
    valuepass=(value,value1,value2,value3,value4,value5,value6)
    result.execute(statement,valuepass)
    establishcon.commit()
    print(messagebox.showinfo(" ","1 row inserted"))
    
    # message=(result.rowcount, " row insert")
    # mse.config(text=message)


    

def updatevalues():
    value=invalue.get()
    value1=invalue1.get()
    establishcon=MyDBConnection()
    result=establishcon.cursor()
    # statement="update student_database set name = (%s) where ID = (%s);"
    # valuepass=(value,value1)
    
    statement="update student_database set name = \""+value1+"\" where ID = "+str(value)+";"
    result.execute(statement)
    establishcon.commit()

    message=(result.rowcount, " row updated")
    mse.config(text=message)


def deletevalues():
    value=invalue.get()
    
    establishcon=MyDBConnection()
    result=establishcon.cursor()
    statement="delete from student_database where ID = (%s);"
    valuepass=(value,)
    result.execute(statement,valuepass)
    establishcon.commit()
    message=(result.rowcount, " row deleted")
    mse.config(text=message)



title=Label(demo,text="STUDENT MARK DETAILS",font="Arial  25 bold ")
title.grid(row=1, column=22)



id=Label(demo,text="ID",font="Arial 15 bold")
id.grid(row=4,column=20,padx=20,pady=20)

invalue=Entry(demo,width=40)
invalue.grid(row=4, column=22)
 


name=Label(demo,text="Name",font="Arial 15 bold")
name.grid(row=5, column=20,padx=20,pady=20)

invalue1=Entry(demo,width=40)
invalue1.grid(row=5, column=22)


taml=Label(demo,text="Language1",font="Arial 15 bold")
taml.grid(row=6, column=20,padx=20, pady=20)

invalue2=Entry(demo,width=40)
invalue2.grid(row=6, column=22)



Engl=Label(demo,text="Language2",font="Arial 15 bold")
Engl.grid(row=7, column=20,padx=20, pady=20)

invalue3=Entry(demo,width=40)
invalue3.grid(row=7, column=22)


math=Label(demo,text="mathametics",font="Arial 15 bold")
math.grid(row=8, column=20,padx=20, pady=20)

invalue4=Entry(demo,width=40)
invalue4.grid(row=8, column=22)


sci=Label(demo,text="Science",font="Arial 15 bold")
sci.grid(row=9, column=20,padx=20, pady=20)

invalue5=Entry(demo,width=40)
invalue5.grid(row=9, column=22)



soci=Label(demo,text="Scocial science",font="Arial 15 bold")
soci.grid(row=10, column=20,padx=20, pady=20)

invalue6=Entry(demo,width=40)
invalue6.grid(row=10, column=22)





insert=Button(demo,text="INSERT",command=insertvalues,font="Arial 11 bold")
insert.grid(row=12, column=21)

update=Button(demo,text="UPDATE",command=updatevalues,font="Arial 11 bold ")
update.grid(row=12, column=22)

delete=Button(demo,text="DELETE",command=deletevalues,font="Arial 11 bold ")
delete.grid(row=14, column=21)

reset=Button(demo,text="RESET",font="Arial 11 bold")
reset.grid(row=14,column=22)

mse=Label(demo,text="   ",font= "Arial 15 bold")
mse.grid(row=15, column=50)














demo.mainloop()
