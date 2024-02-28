import os
from tkinter import *
from tkinter import ttk
from mydbfile import DBManipulate
demo=Tk()
demo.title("Library management system")
demo.geometry("500x500")
dbcon=DBManipulate()
def quit():
    demo.destroy()

def about():
    abt=Tk()
    abt.title("About as")
    abt.geometry("300x300")
    message="""Welcome to libraray management system
    created on :22-02-2024
    by saranya N
    """
    lntinfo=Label(abt,text=message)
    lntinfo.pack()
    abt.mainloop()



    #connection

def inserttoDB():
    stu_id1=str(Ety_Stdid.get())
    stu_name1=str(Ety_StdName.get())
    book_name1=str(Ety_bookname.get())
    author1=str(Ety_author_name.get())
    edition1=str(Ety_Edition.get())
    price1=str(Ety_price.get())
    quantity1=str(Ety_quantity.get())

    x = dbcon.insertvalues(stu_id1,stu_name1,book_name1,author1,edition1,price1,quantity1)
    lblConMsg.config(text=x)
    # selectdatas()


# def selectdatas():

#     data=mydbcon.mydbconnection()
#     result=data.cursor()
#     result.execute("SELECT * FROM borrow_details")
#     i=0 
#     for ai_saranya in result: 
#         for j in range(len(ai_saranya)):
#             lbldisplay = Entry(resultframe, width=10, fg='blue') 
#             lbldisplay.grid(row=i, column=j) 
#             lbldisplay.insert(END, ai_saranya[j])
#         i=i+1 



menubar=Menu(demo)
submenulist=Menu(menubar,tearoff=0)

submenulist.add_command(label="New File", underline=0,accelerator="Ctr+N")
submenulist.add_command(label="New project", underline=7, accelerator="Ctrl+Shift+J")
submenulist.add_command(label="New Py File", underline=5, accelerator="Ctrl+N")

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu, underline=0)

filemenu.add_cascade(label="New",underline=0, accelerator="Ctr+N")
filemenu.add_command(label="Open...",underline=0, accelerator="Ctr+O")
filemenu.add_command(label="Save",underline=0, accelerator="Ctr+S")
filemenu.add_command(label="Save As...",underline=5)
filemenu.add_separator()
filemenu.add_command(label="Page setup...",underline=5)
filemenu.add_command(label="print...",underline=5, accelerator="Ctr+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",underline=0,command=quit)


editmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu,underline=0)

editmenu.add_command(label="Undo", underline=0,accelerator="Crl+Z")
editmenu.add_separator()
editmenu.add_command(label="Cut", underline=0,accelerator="Crl+X")
editmenu.add_command(label="Copy", underline=0,accelerator="Crl+C")
editmenu.add_command(label="Paste", underline=0,accelerator="Ctr+V")
editmenu.add_command(label="Delete", underline=0,accelerator="Del")
editmenu.add_separator()
editmenu.add_command(label="Find", underline=0,accelerator="Crl+F")
editmenu.add_command(label="Find Next", underline=0,accelerator="F3")
editmenu.add_command(label="Replace...", underline=0,accelerator="Crl+H")
editmenu.add_command(label="Go To...", underline=0,accelerator="Ctr+G")
editmenu.add_separator()
editmenu.add_command(label="Select All", underline=0,accelerator="Crl+A")
editmenu.add_command(label="Time/Date", underline=0,accelerator="F5")

formatmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu,underline=0)

formatmenu.add_command(label="Word Wrap", underline=0)
formatmenu.add_command(label="Font...", underline=0)

viewmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu,underline=0)

viewmenu.add_cascade(label="Status Bar", underline=0)

helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)

helpmenu.add_command(label="View Help",underline=0)
helpmenu.add_separator()
helpmenu.add_command(label="About Notepad", underline=0,command=about)









demo.config(menu=menubar)


imgdir1=os.path.join((os.path.join(os.path.dirname(__file__),'img')),"lms.gif")
getTitleImage=PhotoImage('titleimage',file=imgdir1)


# imgdir=os.path.join(os.path.dirname(__file__),'ims')
# getTitleImage=tk.PhotoImage('titleimage',file=os.path.join(imgdir,'lms.gif'))

titleImageFrame=Frame(demo,bg="blue")
titleImageFrame.pack(padx=10,fill="x")

lblDisplayTitleImage=Label(titleImageFrame,image=getTitleImage).pack()

# lblDisplayTitleImage=Label(text="library management system").pack()

tablist=ttk.Notebook(demo)
tablist.pack(padx=10,pady=5)

tabInsert=ttk.Frame(tablist, width=demo.winfo_screenwidth(),height=demo.winfo_screenwidth())
tabInsert.pack()

tabUpdate=ttk.Frame(tablist, width=demo.winfo_screenwidth(),height=demo.winfo_screenwidth())
tabUpdate.pack()

tabDelete=ttk.Frame(tablist, width=demo.winfo_screenwidth(),height=demo.winfo_screenwidth())
tabDelete.pack()

tablist.add(tabInsert,text="Insert")
tablist.add(tabUpdate,text="Update")
tablist.add(tabDelete,text="Delete")

titledisplayframeintab=ttk.Frame(tabInsert,width=demo.winfo_screenwidth(), height=demo.winfo_screenheight())
titledisplayframeintab.pack()

lbl_insertTitle=Label(titledisplayframeintab, text="Inserting Student book_borrow Details")
lbl_insertTitle.grid(pady=10,row=0, columnspan=10)



lbl_Stdid=Label(titledisplayframeintab,text="Student ID")
lbl_Stdid.grid(pady=10,row=1,column=1)
Ety_Stdid=Entry(titledisplayframeintab)
Ety_Stdid.grid(padx=10,pady=10,row=1, column=2)


lbl_Stdname=Label(titledisplayframeintab,text="Name of the student ")
lbl_Stdname.grid(pady=10,row=2,column=1)
Ety_StdName=Entry(titledisplayframeintab)
Ety_StdName.grid(padx=10,pady=10,row=2, column=2)

lbl_bookname=Label(titledisplayframeintab,text="Name of the book ")
lbl_bookname.grid(pady=10,row=3,column=1)
Ety_bookname=Entry(titledisplayframeintab)
Ety_bookname.grid(padx=10,pady=10,row=3, column=2)

lbl_author_name=Label(titledisplayframeintab,text="Name of the Author ")
lbl_author_name.grid(pady=10,row=4,column=1)
Ety_author_name=Entry(titledisplayframeintab)
Ety_author_name.grid(padx=10,pady=10,row=4, column=2)

lbl_Edition=Label(titledisplayframeintab,text="Edition ")
lbl_Edition.grid(pady=10,row=5,column=1)
Ety_Edition=Entry(titledisplayframeintab)
Ety_Edition.grid(padx=10,pady=10,row=5, column=2)

lbl_price=Label(titledisplayframeintab,text="price ")
lbl_price.grid(pady=10,row=6,column=1)
Ety_price=Entry(titledisplayframeintab)
Ety_price.grid(padx=10,pady=10,row=6, column=2)



lbl_quantity=Label(titledisplayframeintab,text="Quantity ")
lbl_quantity.grid(pady=10,row=7,column=1)
Ety_quantity=Entry(titledisplayframeintab)
Ety_quantity.grid(padx=10,pady=10,row=7, column=2)

btn_Insert=Button(titledisplayframeintab, text="Insert",command=inserttoDB)
btn_Insert.grid(row=8,column=1)

btn_Clear=Button(titledisplayframeintab, text="Clear")
btn_Clear.grid(row=8,column=2)

btn_Exit=Button(titledisplayframeintab, text="Quit", command=quit)
btn_Exit.grid(row=8,column=3)

msg=dbcon.mydbconnection()
lblConMsg=Label(titledisplayframeintab, text=msg)
lblConMsg.grid(row=9,column=2, pady=20)

# lblConMsg=Label(titledisplayframeintab, text=" ")


resultframe=Frame(titledisplayframeintab,width=800, height=700,bg="yellow")
resultframe.grid(row=10, columnspan=6)

#updatading details

demo.mainloop()