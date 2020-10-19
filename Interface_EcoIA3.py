from tkinter import *
import picamera
import time
#camera = picamera.PiCamera()

#Functions



#Main Window
def window():
    window = Tk()
    window.title("Main")
    window.geometry('1280x800')
    window.configure(background="Orange")
    Welcome = Label (window, text="Welcome", bg="Orange",fg="Black", font="none 25 bold") .place(relx=0.5, rely=0.1, anchor=CENTER)
    Text1 = Label (window, text="Please press start to dispose of your cigarette filter", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.2, anchor=CENTER)
    Start = Button (window, text="Start", width=5, command = lambda:[window.destroy(),Window2()]) .place(relx=0.5, rely=0.7, anchor=CENTER)
    window.mainloop()


#Page 4
def Window4():
    window4 = Tk()
    window4.title("Thanks")
    window4.geometry('1280x800')
    window4.configure(background="Orange")
    Text5 = Label (window4,text="THANK YOU", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.1, anchor=CENTER)
    Text6 = Label (window4,text="Don't forget your ticket", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.3, anchor=CENTER)
    restart()
   
    

#Page 3
def Window3():
    #camera.capture('/home/pi/Bureau/EcoIA/test_images/Image1.jpg')
    window3 = Tk()
    window3.title("Finish")
    window3.geometry('1280x800')
    window3.configure(background="Orange")
    Text4 = Label (window3,text="Do You want to dispose of another filter?", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.1, anchor=CENTER)
    Yes = Button (window3, text="Yes", width=5, command= lambda:[window3.destroy(),Window2()]) .place(relx=0.7, rely=0.7, anchor=CENTER)
    No = Button (window3, text="No", width=5, command= lambda:[window3.destroy(),Window4()]) .place(relx=0.2, rely=0.7, anchor=CENTER)
 
#Page 2
def Window2():
    window2 = Tk()
    window2.title("Start")
    window2.geometry('1280x800')
    window2.configure(background="Orange")
    Text2 = Label (window2,text="Please insert one cigarette filter on your right", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.1, anchor=CENTER)
    text3 = Label (window2,text="Press Finish when you're done", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.4, anchor=CENTER)
    Finish = Button (window2, text="Finish", width=5, command= lambda:[window2.destroy(),Window3()]) .place(relx=0.5, rely=0.7, anchor=CENTER)
    
def restart():
    window4.destroy()
    window()
    time.sleep(5)
    
window()   



#Labels


#Buttons


#Finish = Button (window2, text="Finish", width=5, command=window3) .place(relx=0.5, rely=0.7, anchor=CENTER)




#main Loop
