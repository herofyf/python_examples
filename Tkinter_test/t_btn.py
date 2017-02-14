import tkinter

#from tkinter import messagebox
import tkinter.messagebox

'''
Tkinter → tkinter
tkMessageBox → tkinter.messagebox
tkColorChooser → tkinter.colorchooser
tkFileDialog → tkinter.filedialog
tkCommonDialog → tkinter.commondialog
tkSimpleDialog → tkinter.simpledialog
tkFont → tkinter.font
Tkdnd → tkinter.dnd
ScrolledText → tkinter.scrolledtext
Tix → tkinter.tix
ttk → tkinter.ttk
'''
top = tkinter.Tk()

def helloCallBack():
    tkinter.messagebox.showinfo("hello world", "hello world")

btn = tkinter.Button(top, text ="hello", command=helloCallBack)
btn.pack()

top.mainloop()