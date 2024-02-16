from tkinter import *

app=Tk()
app.title("Calculator")
app.geometry("500x500+100+100")
app.config(bg="yellow")

def addition():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a+b
    outputbox.config(text=c)

def subtraction():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a-b
    outputbox.config(text=c)

def multiplication():
    a=int(inputbox1.get())
    b=int(inputbox2.get())
    c=a*b
    outputbox.config(text=c)


def division():
    a=float(inputbox1.get())
    b=float(inputbox2.get())
    c=a/b
    outputbox.config(text=c)

def modulas():
    a=float(inputbox1.get())
    b=float(inputbox2.get())
    c=a%b
    outputbox.config(text=c)

def power():
    a=int(inputbox2.get())
    b=int(inputbox1.get())
    c=a ** b
    outputbox.config(text=c)

def floordivision():
    a=int(inputbox2.get())
    b=int(inputbox1.get())
    c=a // b
    outputbox.config(text=c)

def equal():
    a=int(inputbox2.get())
    b=int(inputbox1.get())
    c=a == b
    outputbox.config(text=c)

def increement():
    a=int(inputbox2.get())
    b=int(inputbox1.get())
    a+=b
    outputbox.config(text=a)

def decreement():
    a=int(inputbox2.get())
    b=int(inputbox1.get())
    a-=b
    outputbox.config(text=a)

def greaterequl():
    a=int(inputbox2.get())
    b=int(inputbox1.get())
    a>>=b
    outputbox.config(text=a)

def lessthenequl():
    a=int(inputbox2.get())
    b=int(inputbox1.get())
    a<<=b
    outputbox.config(text=a)
def And ():
    a=int(inputbox2.get())
    b=int(inputbox1.get())
    c=a & b
    outputbox.config(text=a)

def Or ():
    a=int(inputbox2.get())
    b=int(inputbox1.get())
    c=a | b
    outputbox.config(text=a)













    
lbltitle=Label(app,text="arithmetic programs",font="Arial 20 bold")
lbltitle.grid(row=0,column=21, padx=20, pady=20)

    

lblTitle1=Label(app,text="Enter the value a:",font="Arial 20 bold")
lblTitle1.grid(row=2, column=20, padx=20, pady=20)

inputbox1=Entry(app,width=30)
inputbox1.grid(row=2, column=25)

    
lableTitle2=Label(app,text="Entr the value b:",font="Arial 20 bold")
lableTitle2.grid(row=3, column=20, padx=20, pady=20)

inputbox2=Entry(app,width=30)
inputbox2.grid(row=3, column=25)

outputbox=Label(app,text="     ")
outputbox.grid(row=4, column=25, padx=40, pady=40)



clickme=Button(app,text="+",command=addition,font="Arial 10 bold")
clickme.grid(row=4,column=20)

clickme=Button(app,text="-",command=subtraction ,font="Arial 20 bold")
clickme.grid(row=4,column=21)

clickme=Button(app,text="*",command=multiplication,font="Arial 20 bold")
clickme.grid(row=5,column=20)

clickme=Button(app,text="/",command=division,font="Arial 20 bold")
clickme.grid(row=5,column=21)


clickme=Button(app,text="%",command=modulas,font="Arial 20 bold")
clickme.grid(row=5,column=21, padx=40, pady=40)

clickme=Button(app,text="X^2",command=power,font="Arial 20 bold")
clickme.grid(row=4,column=22, padx=40, pady=40)

clickme=Button(app,text="//",command=floordivision,font="Arial 20 bold")
clickme.grid(row=4,column=23, padx=40, pady=40)

clickme=Button(app,text="==",command=equal,font="Arial 20 bold")
clickme.grid(row=5,column=24, padx=40, pady=40)

clickme=Button(app,text="+=",command=increement,font="Arial 20 bold")
clickme.grid(row=5,column=22, padx=40, pady=40)

clickme=Button(app,text="-=",command=decreement,font="Arial 20 bold")
clickme.grid(row=5,column=23, padx=40, pady=40)


clickme=Button(app,text=">>=",command=greaterequl,font="Arial 20 bold")
clickme.grid(row=6,column=20, padx=40, pady=40)

clickme=Button(app,text="<<=",command=lessthenequl,font="Arial 20 bold")
clickme.grid(row=6,column=21, padx=40, pady=40)


clickme=Button(app,text="&",command=And,font="Arial 20 bold")
clickme.grid(row=6,column=22, padx=40, pady=40)

clickme=Button(app,text="|",command=Or,font="Arial 20 bold")
clickme.grid(row=6,column=23, padx=40, pady=40)
















app.mainloop()
