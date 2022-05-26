from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pyodbc
import credentials as cr

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("900x900")
        self.window.config(bg = "white")




        frame = Frame(self.window, bg="white")
        frame.place(x=350,y=100,width=500,height=550)

        title1 = Label(frame, text="Sign Up", font=("times new roman",25,"bold"),bg="white").place(x=20, y=10)
        title2 = Label(frame, text="Join with us", font=("times new roman",13),bg="white", fg="gray").place(x=20, y=50)

        f_name = Label(frame, text="Username", font=("helvetica",15,"bold"),bg="white").place(x=20, y=100)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        password =  Label(frame, text="New password", font=("helvetica",15,"bold"),bg="white").place(x=20, y=240)

        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=270, width=420)



if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()

