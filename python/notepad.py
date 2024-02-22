import tkinter as tk
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

filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu, underline=0)

filemenu.add_command(label="New",underline=0, accelerator="Ctr+N")
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
demo.mainloop()