import mysql.connector
from tkinter import *
class DBManipulate:
    def __init__(self):
        print("Welcome to DB manipulation")

    def returnMsg(self):
        return "connected"
        

    def mydbconnection(self):
        con=mysql.connector.connect(
        host="192.168.1.240",
        user="AIBATCH01",
        password="AI@123",
        database="ai_saranya"
        )
        return con


    def insertvalues(self,stu_id,stu_name,book_name,author,edition,price,quatity):
        stu_id1=stu_id
        stu_name1=stu_name
        book_name1=book_name
        author1=author
        edition1=edition
        price1=price
        quantity1=quatity
    # def insertvalues(self):
    #     stu_id1=1
    #     stu_name1="saranya"
    #     book_name1="tamil"
    #     author1="arun"
    #     edition1="2nd"
    #     price1=123
    #     quantity1=1

        data=self.mydbconnection()
        result=data.cursor()

        stmts="INSERT INTO borrow_details(stu_id, stu_name,book_name,author,edition,price,quantity) VALUES("+str(stu_id1)+ ", "+ '"' + stu_name1 + '"' + ","+ '"' + book_name1 + '"' + ","+ '"' + author1 + '"'  + ","+  '"' + edition1 + '"' + "," + str(price1)+" , "+str(quantity1)+");)"
        # value=(stu_id1,stu_name1,book_name1,author1,edition1,price1,quantity1)
        result.execute(stmts)
        print(stmts)



        data.commit()

        return (str(result.rowcount) + " row inserted")


    # def selectdatas(self):

    #     data=self.mydbconnection()
    #     result=data.cursor()
    #     result.execute("SELECT * FROM borrow_details")
    #     i=0 
    #     for ai_saranya in result: 
    #          for j in range(len(ai_saranya)):
    #              lbldisplay = Label(self, width=10, fg='blue') 
    #              lbldisplay.grid(row=i, column=j) 
    #              lbldisplay.insert(END, ai_saranya[j])
    #          i=i+1