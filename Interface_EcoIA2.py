import tkinter
from tkinter import *
import picamera
import cv2
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
pwm=GPIO.PWM(18,100)


ajoutAngle = 5



root=tkinter.Tk()


num = StringVar()
tnum = StringVar()
X = 0
root.title("Main")
root.geometry('1280x800')
root.configure(background="Orange")
Welcome = Label (root, text="Welcome", bg="Orange",fg="Black", font="none 25 bold") .place(relx=0.5, rely=0.1, anchor=CENTER)
Text1 = Label (root, text="Please press start to dispose of your cigarette filter", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.2, anchor=CENTER)
    
    

#photo= PhotoImage(file="start.jpg")
btn = Button(root, text= "Start", width=5, bg='Orange', command= lambda: [Window2(),Sopen()]) .place(relx=0.5, rely=0.7, anchor=CENTER)
             


#Page 4
def Window4():
    window4 = Tk()
    window4.title("Thanks")
    window4.geometry('1280x800')
    window4.configure(background="Orange")
    Text5 = Label (window4,text="THANK YOU", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.1, anchor=CENTER)
    Text6 = Label (window4,text="Don't forget your ticket", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.3, anchor=CENTER)
    window4.after(3000, lambda : window4.destroy())
    

    
#Page 3
def Window3():
    #camera.capture('/home/pi/Bureau/EcoIA/test_images/Image1.jpg')
    window3 = Toplevel()
    window3.title("Finish")
    window3.geometry('1280x800')
    window3.configure(background="Orange")
    Text5 = Label (window3,text="You have disposed of ", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.39, rely=0.1, anchor=CENTER)
    Text6 = Label (window3,textvariable= num, bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.1, anchor=CENTER)
    Text7 = Label (window3,text=" cigarette butts ", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.58, rely=0.1, anchor=CENTER)
    
    #Text4 = Label (window3,text="Do You want to dispose of another filter?", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.3, anchor=CENTER)
    #Yes = Button (window3, text="Yes", width=5, command= lambda:[window3.after(1000, lambda : window3.destroy()),Window2()]) .place(relx=0.7, rely=0.7, anchor=CENTER)
    No = Button (window3, text="Ok", width=5, command= lambda:[Window4(),Sneutral(),window3.after(1000, lambda : window3.destroy())]) .place(relx=0.2, rely=0.7, anchor=CENTER)
  
#Page 2
def Window2():
    window2=Toplevel()
    window2.title("Start")
    window2.geometry("1280x800")
    window2.configure(background="Orange")
    Text2 = Label (window2,text="Please insert one cigarette filter on your right", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.1, anchor=CENTER)
    text3 = Label (window2,text="Press Finish when you're done", bg="Orange",fg="Black", font="none 15 bold") .place(relx=0.5, rely=0.4, anchor=CENTER)
    Back = Button(window2, text="Back", width=5, command= window2.destroy) .place(relx=0.2, rely=0.7, anchor=CENTER)
    Finish = Button(window2, text="Finish", width=5, command= lambda:[Window3(),Sclosed(),Vib(),detection(), window2.after(1000, lambda : window2.destroy())]) .place(relx=0.7, rely=0.7, anchor=CENTER)
    

def Sopen():
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(18, GPIO.OUT)
    #pwm=GPIO.PWM(18,100)
    angle = 180
    duree = 0.1
    pwm.start(5)
    angleChoisi = angle/10 + ajoutAngle
    pwm.ChangeDutyCycle(angleChoisi)
    time.sleep(duree)
    pwm.stop()
    GPIO.cleanup()
    
def Sclosed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setwarnings(False)
    pwm=GPIO.PWM(18,100)
    angle = 0
    duree = 0.1
    pwm.start(5)
    angleChoisi = angle/10 + ajoutAngle
    pwm.ChangeDutyCycle(angleChoisi)
    time.sleep(duree)
    pwm.stop()
    GPIO.cleanup()
    
def Vib():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setwarnings(False)
    duree = 0.04

    pwm2=GPIO.PWM(17,100)
    pwm2.start(5)
    
    ajoutAngle = 5
    i = 0

    while i <= 20 :
        pwm2.ChangeDutyCycle(11)
        time.sleep(duree)
        pwm2.ChangeDutyCycle(12.5)
        time.sleep(duree)
        pwm2.ChangeDutyCycle(11)
        time.sleep(duree)
        i = i + 1
    pwm2.ChangeDutyCycle(12)
    time.sleep(0.1)
    pwm2.stop()
    GPIO.cleanup()

def Sneutral():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    pwm2=GPIO.PWM(17,100)
    pwm2.start(5)
    pwm2.ChangeDutyCycle(11.5)
    time.sleep(0.1)
    pwm2.stop()
    GPIO.cleanup()
    
    
#def Sout():
#    if X != "0":
#        GPIO.setmode(GPIO.BCM)
#        GPIO.setup(17, GPIO.OUT)
#        pwm2=GPIO.PWM(17,100)
#        pwm2.start(5)
#        pwm2.ChangeDutyCycle(20)
#        time.sleep(0.1)
#        pwm2.stop()
#        GPIO.cleanup()
#        print("in")
#        print(X)
#    elif X == "0":
#        GPIO.setmode(GPIO.BCM)
#        GPIO.setup(17, GPIO.OUT)
#        pwm2=GPIO.PWM(17,100)
#        pwm2.start(5)
#        pwm2.ChangeDutyCycle(4)
#        time.sleep(0.1)
#        pwm2.stop()
#        GPIO.cleanup()
#        print("out")
#        print(X)
        
    
def detection():
    classNames = {0: 'background',
              1: 'Person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
              7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
              13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
              18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
              24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
              32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
              37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
              41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
              46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
              51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
              56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
              61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
              67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
              75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
              80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
              86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}


    def id_class_name(class_id, classes):
        for key, value in classes.items():
            if class_id == key:
                return value


# Loading model
    model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                      'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
#camera = picamera.PiCamera()
#camera.resolution = (300, 300)
#camera.capture('/home/pi/Bureau/EcoIA/ExploreOpencvDnn/Image5.jpg')

    image = cv2.imread("image6.jpg")

    image_height, image_width, _ = image.shape

    model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
    output = model.forward()
    X = 0
    Y = 0 
    for detection in output[0, 0, :, :]:
        confidence = detection[2]
        if confidence > .6:
            class_id = detection[1]
            class_name=id_class_name(class_id,classNames)
            print(str(str(class_id) + " " + str(detection[2])  + " " + class_name))
            if class_id == 1.0 :
                X = X + 1
                Y = Y +1
#            box_x = detection[3] * image_width
#            box_y = detection[4] * image_height
#            box_width = detection[5] * image_width
#            box_height = detection[6] * image_height
#            cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=1)
#            cv2.putText(image,class_name ,(int(box_x), int(box_y+.05*image_height)),cv2.FONT_HERSHEY_SIMPLEX,(2),(0, 0, 255))

    if X > 0:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        pwm2=GPIO.PWM(17,100)
        pwm2.start(5)
        pwm2.ChangeDutyCycle(20)
        time.sleep(0.1)
        pwm2.stop()
        GPIO.cleanup()
        print("in")
        print(X)
    else:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        pwm2=GPIO.PWM(17,100)
        pwm2.start(5)
        pwm2.ChangeDutyCycle(4)
        time.sleep(0.1)
        pwm2.stop()
        GPIO.cleanup()
        print("out")
        print(X)
    
    print(X)
    num.set(X)
    



    
#root()     
#root.mainloop()

#def restart():
#    window4.destroy()
#    window()
#    time.sleep(5)
#    
#window()   



#Labels


#Buttons


#Finish = Button (window2, text="Finish", width=5, command=window3) .place(relx=0.5, rely=0.7, anchor=CENTER)




#main Loop
