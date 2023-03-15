import tkinter 
import cv2
import PIL.Image, PIL.ImageTk

SET_WIDTH = 680
SET_HEIGHT = 368
#tkinter gui yha se start hogi
window = tkinter.Tk()
window.title("manav 1st project DRS system")
cv_img =cv2.cvtColor(cv2.imread("wlcm.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width = SET_WIDTH, height= SET_HEIGHT)
#image ko canvas m dalna h mtlb background image
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0, ancho = tkinter.NW , image = photo,)
canvas.pack()
window.mainloop()
printf("hello")