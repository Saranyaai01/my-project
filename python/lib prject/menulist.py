import os
import tkinter as tk
win=tk.Tk()
win.geometry("500x500")
win.title("Library management system")
menubar=tk.Menu(win)
filemenu=tk.Menu(menubar,tearoff=0 )
menubar.add_cascade(label="File",menu=filemenu)
editmenu=tk.Menu(menubar,tearoff=0)
win.config(menu=menubar)
win.mainloop()
