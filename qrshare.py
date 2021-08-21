
import tkinter as tk

def main():
    window = tk.Tk()
    window.title('QRShare')
    window.geometry('1395x933')
    window.configure(bg='#FFFFFF')

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

    window.mainloop()
if __name__ == '__main__':
    main()
