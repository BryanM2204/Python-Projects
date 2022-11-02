import math
import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text = "1").grid(row = 0, column = 0)
ttk.Button(frm, text = "2").grid(row = 0, column = 1)
ttk.Button(frm, text = "3").grid(row = 0, column = 2)

ttk.Button(frm, text = "4").grid(row = 1, column = 0)
ttk.Button(frm, text = "5").grid(row = 1, column = 1)
ttk.Button(frm, text = "6").grid(row = 1, column = 2)

ttk.Button(frm, text = "7").grid(row = 2, column = 0)
ttk.Button(frm, text = "8").grid(row = 2, column = 1)
ttk.Button(frm, text = "9").grid(row = 2, column = 2)

ttk.Button(frm, text = "0").grid(row = 3, column = 0)
ttk.Button(frm, text = ".").grid(row = 3, column = 1)
ttk.Button(frm, text = "+/-").grid(row = 3, column = 2)

root.mainloop()
