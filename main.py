import tkinter 
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
#threading use ki taaki hmara program hang na kre
import threading
import imutils
import time

stream = cv2.VideoCapture("clip2.mp4")
def play(speed):
    print(f"you clicked on play.Speed is {speed}")

 #play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1+ speed)

    
    grabbed, frame = stream.read()
    frame = imutils.resize(frame, width=200, height=200)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image= frame, anchor=tkinter.NW)


def pending(decision):
    #1. Diplay decision pending image
    #2. wait for a second
    #3. display sponsr image 
    #4.display out /not out"""
    frame = cv2.cvtColor(cv2.imread("decisionpend.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH ,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image= frame, anchor= tkinter.NW)

    time.sleep(1.5)

    frame = cv2.cvtColor(cv2.imread("jiospon.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH ,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image= frame, anchor= tkinter.NW)

    time.sleep(2.5)

    if   decision =='outt':
           decisionImg = "outt.jpg"
    else:
        decisionImg = "notoutt.jpg"     
    frame =cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width = SET_WIDTH ,height = SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image= frame, anchor= tkinter.NW)


def out():
    thread = threading.Thread(target= pending, args =("outt",))
    thread.daemon = 1
    thread.start()
    print("out")

def not_out():
     thread = threading.Thread(target= pending, args =("notoutt",))
     thread.daemon = 1
     thread.start()
     print("not_out")
SET_WIDTH = 680
SET_HEIGHT = 368
#tkinter gui yha se start hogi
window = tkinter.Tk()
window.title("manav 1st project DRS system")
cv_img =cv2.cvtColor(cv2.imread("wlcmto.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width = SET_WIDTH, height= SET_HEIGHT)
#image ko canvas m dalna h mtlb background image
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img),width = SET_WIDTH,height=SET_HEIGHT)
image_on_canvas = canvas.create_image(0,0, ancho = tkinter.NW , image = photo)
canvas.pack()


#control button for playback
btn = tkinter.Button(window, text = "<< Previous(Fast)",width = 50,command= partial(play,-25))
btn.pack()
btn = tkinter.Button(window, text = "<< Previous(slow)",width = 50,command= partial(play,-2))
btn.pack()
btn = tkinter.Button(window, text = " Next(slow)>>",width = 50,command= partial(play,2))
btn.pack()
btn = tkinter.Button(window, text = " Next(fast)>>",width = 50,command= partial(play,25))
btn.pack()
btn = tkinter.Button(window, text = " Give out ",width = 50,command= out)
btn.pack()
btn = tkinter.Button(window, text = "Give notout",width = 50,command=not_out)
btn.pack()
window.mainloop()