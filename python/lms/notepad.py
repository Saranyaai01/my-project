import tkinter as tk
from tkinter import ttk
import os
demo=tk.Tk()
demo.geometry("500x500")
demo.title("Untitled-Notepad")

def quit():
    demo.destroy()

def about():
    abt=tk.Tk()
    abt.title("About as")
    abt.geometry("300x300")
    message="""Welcome to Notepad text editor
    created on :22-02-2024
    by saranya N
    """
    lntinfo=tk.Label(abt,text=message)
    lntinfo.pack()
    abt.mainloop()


menubar=tk.Menu(demo)
submenulist=tk.Menu(menubar,tearoff=0)

submenulist.add_command(label="New File", underline=0,accelerator="Ctr+N")
submenulist.add_command(label="New project", underline=7, accelerator="Ctrl+Shift+J")
submenulist.add_command(label="New Py File", underline=5, accelerator="Ctrl+N")

filemenu=tk.Menu(menubar,tearoff=0)
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


editmenu=tk.Menu(menubar, tearoff=0)
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

formatmenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu,underline=0)

formatmenu.add_command(label="Word Wrap", underline=0)
formatmenu.add_command(label="Font...", underline=0)

viewmenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu,underline=0)

viewmenu.add_cascade(label="Status Bar", underline=0)

helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)

helpmenu.add_command(label="View Help",underline=0)
helpmenu.add_separator()
helpmenu.add_command(label="About Notepad", underline=0,command=about)









demo.config(menu=menubar)

# imgdir=os.path.join(os.path.dirname(__file__),'ims')
# getTitleImage=tk.PhotoImage('titleimage',file=os.path.join(imgdir,'ims.gif'))

titleImageFrame=tk.Frame(demo,bg="blue")
titleImageFrame.pack(padx=10,fill="x")

# lblDisplayTitleImage=tk.Label(titleImageFrame,image=getTitleImage).pack()

lblDisplayTitleImage=tk.Label(text="library management system").pack()

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

lbl_insertTitle=tk.Label(titledisplayframeintab, text="Inserting Student Details")
lbl_insertTitle.grid(pady=10,row=0, columnspan=10)



lbl_StdName=tk.Label(titledisplayframeintab,text="Name of the student ")
lbl_StdName.grid(pady=10,row=1,column=1)
Ety_StdName=tk.Entry(titledisplayframeintab)
Ety_StdName.grid(padx=10,pady=10,row=1, column=2)


lbl_Stdid=tk.Label(titledisplayframeintab,text="Roll Number ")
lbl_Stdid.grid(pady=10,row=2,column=1)
Ety_Stdid=tk.Entry(titledisplayframeintab)
Ety_Stdid.grid(padx=10,pady=10,row=2, column=2)

lbl_bookname=tk.Label(titledisplayframeintab,text="Name of the book ")
lbl_bookname.grid(pady=10,row=3,column=1)
Ety_bookname=tk.Entry(titledisplayframeintab)
Ety_bookname.grid(padx=10,pady=10,row=3, column=2)

lbl_author_name=tk.Label(titledisplayframeintab,text="Name of the Author ")
lbl_author_name.grid(pady=10,row=4,column=1)
Ety_author_name=tk.Entry(titledisplayframeintab)
Ety_author_name.grid(padx=10,pady=10,row=4, column=2)

lbl_Edition=tk.Label(titledisplayframeintab,text="Edition ")
lbl_Edition.grid(pady=10,row=5,column=1)
Ety_Edition=tk.Entry(titledisplayframeintab)
Ety_Edition.grid(padx=10,pady=10,row=5, column=2)



lbl_quantity=tk.Label(titledisplayframeintab,text="Quantity ")
lbl_quantity.grid(pady=10,row=6,column=1)
Ety_quantity=tk.Entry(titledisplayframeintab)
Ety_quantity.grid(padx=10,pady=10,row=6, column=2)

btn_Insert=tk.Button(titledisplayframeintab, text="Insert")
btn_Insert.grid(row=7,column=1)

btn_Clear=tk.Button(titledisplayframeintab, text="Clear")
btn_Clear.grid(row=7,column=2)

btn_Exit=tk.Button(titledisplayframeintab, text="Quit", command=quit)
btn_Exit.grid(row=7,column=3)




demo.mainloop()