# Author: Kesavan M
# github: github.com/K7esavan
# description:
#   Desktop application that let you create QR Code inserted with data

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import PIL
from PIL import Image, ImageTk
import qrcode
import cv2
import platform

operating_system = platform.system()

def getQRCodeFileName():
    if operating_system == 'Windows':
        dir = '/'
    else:
        dir = '/home'
    return filedialog.askopenfilename(
        initialdir=dir,
        title='Select the file',
        filetypes=(('PNG files', '*.png'),
                   ('JPG files', '*.jpg'),
                   ('JPEG files','*.jpeg'))
    )


window = tk.Tk()
window.title('QRShare')
window.geometry('1395x933')
window.configure(bg='#FFFFFF')
logo = tk.PhotoImage('./resources/logo.ico')
window.iconphoto(False, logo)
window.resizable(False, False)

canvas = tk.Canvas(
        master=window,
        height=933,
        width=1395,
        highlightthickness=0,
        bd=0,
        background="#FFFFFF",
        relief='ridge')
canvas.place(x=0, y=0)

# For welcome message
canvas.create_rectangle(0.0, 0.0, 707.0, 933.0, fill='#00EDA6', outline='')

# For getting input
canvas.create_rectangle(707.0, 0.0, 1395.0, 933.0, fill='#FFFFFF', outline='')


def displayData():
    # we need to find the location of the file
    filename = getQRCodeFileName()
    detector = cv2.QRCodeDetector()
    data, points, straight_qrcode = detector.detectAndDecode(cv2.imread(filename))
    messagebox.showinfo(title='QRCode Data', message=data)

# Select (Button)
select_button_image = tk.PhotoImage(file='./resources/buttons/select_btn.png')
select_button = tk.Button(
    master=window,
    image=select_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=displayData,
    relief='flat'
)

select_button.place(x=780.0, y=544.0)

# Exit (Button)
exit_button_image = tk.PhotoImage(file='./resources/buttons/exit_btn.png')
exit_button = tk.Button(
    master=window,
    image=exit_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief='flat'
)

exit_button.place(x=960.0, y=786.0)

# GENERATE QR (Label)
genImage = ImageTk.PhotoImage(Image.open('./resources/generateqr.png'))
generateLabel = tk.Label(master=window,
                         background='#FFFFFF',
                         image=genImage)
generateLabel.place(x=750, y=20, width=200, height=40)

# READ QR (Label)
scanqrImage = ImageTk.PhotoImage(Image.open('./resources/readqr.png'))
scanqrLabel = tk.Label(master=window,
                       background='#FFFFFF',
                       image=scanqrImage)
scanqrLabel.place(x=740, y=400, width=200, height=40)

# Entry Box
inputText = tk.Text(
            master=window,
            height=10,
            width=60,
            relief=tk.GROOVE)
inputText.place(x=800, y=70)

# Submit Button
def generateQR():
    try:
        img = qrcode.make(data=inputText.get('1.0', tk.END))
        if operating_system == 'Windows':
            choosenfilelocation =  filedialog.asksaveasfilename(
                    initialdir='/', filetypes=(('PNG Files', '*.png'), ('JPG Files', '*jpg')))
        else:
            choosenfilelocation =  filedialog.asksaveasfilename(
                    initialdir='/home', filetypes=(('PNG Files', '*.png'), ('JPG Files', '*jpg')))
        print ("written in :" +choosenfilelocation)
        img.save(choosenfilelocation)
        inputText.delete('1.0', tk.END)
        messagebox.showinfo(title='Information', message='QR Code Generated Successfully')
    except:
        messagebox.showerror(title='Something went wrong', message='Couldn\'t Generate QR Code')

sbtn_img = ImageTk.PhotoImage(Image.open('./resources/buttons/submit.png'))
text_sub_btn = tk.Button(master=window, 
                         image=sbtn_img,
                         relief=tk.FLAT,
                         highlightthickness=0,
                         background='#FFFFFF',
                         bd=0,
                         command=generateQR)
text_sub_btn.place(x = 960, y=300)

sel_file_label = tk.Label(master=window, text='Select the QR Image', font=('Arial', 13), 
                          background='#FFFFFF')
sel_file_label.place(x=780, y=500)


# Welcome message (Label)
welcomeMessage = ImageTk.PhotoImage(Image.open('./resources/welcomeMessage.png'))
welcome_label = tk.Label(
        master=window,
        height=500,
        width=500,
        image=welcomeMessage,
        background="#00EDA6")
welcome_label.place(x = 50, y=100)

# About Me (Label)
tk.Label(master=window,
         text='Kesavan M ',
         background='#00EDA6',
         fg='#FFFFFF',
         font=('Arial', 14, 'bold')).place(x=100, y=700)
tk.Label(master=window, 
         text='github/k7esavan',
         background='#00EDA6',
         fg='#FFFFFF',
         font=('Arial', 14, 'bold')).place(x=100, y=730)

window.mainloop()

