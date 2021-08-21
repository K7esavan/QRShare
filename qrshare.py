
import tkinter as tk
from tkinter import filedialog
import PIL
from PIL import Image, ImageTk
import qrcode
import cv2

def getQRCodeFileName():
    return filedialog.askopenfilename(
        initialdir='/',
        title='Select the file',
        filetypes=(('PNG files', '*.png'),
                   ('JPG files', '*.jpg'),
                   ('JPEG files','*.jpeg'))
    )

def getFileName():
    return filedialog.askopenfilename(initialdir='/')

def writeDataIntoFile(outputfile):
    pass

def main():
    window = tk.Tk()
    window.title('QRShare')
    window.geometry('1395x933')
    window.configure(bg='#FFFFFF')
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

    select_button_image = tk.PhotoImage(file='./resources/buttons/select_btn.png')
    exit_button_image = tk.PhotoImage(file='./resources/buttons/exit_btn.png')

    select_button = tk.Button(
        master=window,
        image=select_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=getQRCodeFileName,
        relief='flat'
    )

    exit_button = tk.Button(
        master=window,
        image=exit_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=window.destroy,
        relief='flat'
    )

    select_button.place(
        x=753.0,
        y=544.0
    )

    exit_button.place(
        x=753.0,
        y=686.0
    )

    # Welcome message
    welcomeMessage = ImageTk.PhotoImage(Image.open('./resources/welcomeMessage.png'))
    welcome_label = tk.Label(
            master=window,
            height=500,
            width=500,
            image=welcomeMessage)
    welcome_label.place(x = 50, y=10)

    window.mainloop()
if __name__ == '__main__':
    main()
