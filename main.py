import os.path
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import cv2

co0 = "#ffffff"  # WHITE
co1 = "#000000"  # BLACK
co2 = "#63b9ff"  # BLUE

window = Tk()
window.title("")
window.geometry("300x356")
window.configure(background=co0)
window.resizable(width=False, height=False)

global l_img, img, orignal_img, saved_name
orignal_img = []


def choose_img():
    global l_img, img, orignal_img, saved_name

    img = fd.askopenfilename()
    print(img)
    saved_name = os.path.split(img)[-1]
    print(saved_name)
    orignal_img.append(img)

    img = Image.open(img)

    img = img.resize((110, 200))
    img = ImageTk.PhotoImage(img)
    l_img = Label(window, image=img, bg=co0, fg=co1)
    l_img.place(x=60, y=60)


def covert_img():
    global l_img, img, orignal_img, saved_name
    scale_value = scale.get()
    # load the choosen image

    img = cv2.imread(orignal_img[-1])

    # convert one colorspace to another
    convert_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(convert_img, (25, 25), 300, 300)
    img_to_sketch = cv2.divide(convert_img, blurred_img, scale=scale_value)

    file_name, file_extension = os.path.splitext(saved_name)
    new_file_name = file_name + "_pencil_sketch" + file_extension

    cv2.imwrite(new_file_name, img_to_sketch)
    print("Saved the image as:", new_file_name)

    # cv2.imwrite(saved_name, img_to_sketch)
    # print("save the image")

    img = Image.open(new_file_name)
    img = img.resize((110, 200))
    img = ImageTk.PhotoImage(img)
    l_img = Label(window, image=img, bg=co0, fg=co1)
    l_img.image = img  # Keep a reference to the image to prevent garbage collection
    l_img.place(x=60, y=60)


def printname():
    print('Hello bhai log')


# def open_img(img):
#     global orignal_img, l_img
#     img = Image.open(img)
#     img = img.resize((110, 200))
#     img = ImageTk.PhotoImage(img)
#
#     l_img = Label(window, image=img, bg=co0, fg=co1)
#     l_img.place(x=60, y=60)


style = ttk.Style(window)
style.theme_use("clam")

app_image = Image.open("icons8-pencil-100.png")
app_image = app_image.resize((50, 50))
app_image = ImageTk.PhotoImage(app_image)

app_logo = Label(window, image=app_image, text="image to sketch", width=1020, compound=LEFT, relief=RAISED, anchor=NW,
                 font='System 15 bold', background=co0, fg=co1)
app_logo.place(x=0, y=0)

l_option = Label(window, text='setting---------------------------------------------------'.upper(), anchor=NW,
                 font='verdana 7 bold', bg=co0, fg=co1)
l_option.place(x=10, y=260)

scale = Scale(window, from_=0, to=255, length=120, bg=co0, fg='Red', orient=HORIZONTAL)
scale.place(x=10, y=287)

b_choose = Button(window, text='choose img', command=choose_img, width=15, overrelief=RAISED, font='Ivy 10', bg=co2,
                  fg=co1)
b_choose.place(x=147, y=287)

save_choose = Button(window, text='save img', command=covert_img, width=15, overrelief=RAISED, font='Ivy 10', bg=co2, fg=co1)
save_choose.place(x=147, y=317)

window.mainloop()
