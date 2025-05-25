import Bio
from Bio.Seq import Seq
import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import time
from math import *
from start import solarsytem
import turtle

root = tk.Tk()
root.geometry('700x550')
root.config(highlightbackground='green')
root.title('Contact Book')


DNA_Strand = StringVar()
MRNA = StringVar()
PROTIEN = StringVar()


def draw():
    turtle.title('hello')
    turtle.bgcolor('pink')
    turtle.pencolor('blue')
    turtle.circle(55)
    turtle.pencolor('red')
    turtle.circle(10)
    turtle.teleport(150, 200)
    turtle.circle(50)
    turtle.fillcolor()

    turtle.mainloop()


def mrnawin():
    win2 = tk.Tk()
    win2.title('MRNA')
    win2.config(highlightbackground="pink")
    win2.state('zoomed')

    win2.mainloop()


def bar():
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100

    progress['value'] = 0


def convert():
    messagebox.askquestion("confirmation", "Do you want to convert this into protien ")
    bar()
    cdna = Seq(ent.get())
    mrna = cdna.transcribe()
    MRNA.set(str(mrna))
    prot = mrna.translate()
    PROTIEN.set(str(prot))
    messagebox.showinfo("Confirmation", "DNA_STRAND converted to protien succesfully")


menubutton = Menubutton(root, text="Menu")
menubutton.menu = Menu(menubutton)
menubutton["menu"] = menubutton.menu
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
menubutton.menu.add_command(activebackground='black', command=draw, label="test")
menubutton.menu.add_command(label='mrna', activeforeground="black", state="active", command=mrnawin)
menubutton.menu.add_command(label='Solar system', activeforeground="lightblue", state="normal")

menubutton.pack()
Label(root, text='Dna_Strand', font=("Times new roman", 25, "bold"), bg='SlateGray3').place(x=30, y=20)
ent = tk.Entry(root, textvariable=DNA_Strand, width=50)
ent.place(x=220, y=30)
Label(root, text='MRNA', font=("Times new roman", 20, "bold"), bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=MRNA, width=50).place(x=200, y=80)
Label(root, text='PROTIEN', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=120)
Entry(root, textvariable=PROTIEN, width=50).place(x=200, y=125)

progress = Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
progress.place(x=100, y=250)
Button(root, text="FIND", font='Helvetica 18 bold', bg='#e8c1c7', command=lambda: convert(), padx=20).place(x=50, y=300)
root.mainloop()
