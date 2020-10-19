from tkinter import *

def Window2():
    top = Toplevel()
    window.destroy()
    top.title("window2")
    top.geometry('800x480')
    Finish = Button (top, text="Finish", width=5, command= top.destroy) .place(relx=0.5, rely=0.7, anchor=CENTER)


window = Tk()
window.title("Main")
window.geometry('800x480')
window.configure(background="Orange")
Start = Button (window, text="Start", width=5, command = Window2) .place(relx=0.5, rely=0.7, anchor=CENTER)