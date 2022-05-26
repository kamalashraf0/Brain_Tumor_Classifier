from tkinter import *
from PIL import ImageTk, Image

class clas():
    def __init__(self):
        # Create an instance of tkinter window
        self.win = Tk()

        # Define the geometry of the window
        self.win.geometry("700x500")

        frame = Frame(self.win, width=600, height=400)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        # Create an object of tkinter ImageTk
        img = ImageTk.PhotoImage(Image.open(r"E:\SSD\Uni\Graduation Project\Brain Dataset\Test\no\no.jpg"))

        # Create a Label Widget to display the text or Image
        text = "A brain tumor is an abnormal growth of cells inside\n the brain or skull; some are benign, others malignant.\n" \
               " Tumors can grow from the brain tissue itself (primary),\n or cancer from elsewhere in the body can spread to\n the brain (metastasis)." \
               " Treatment options vary\n depending on the tumor type, size and location."
        label = Label(frame, text=text, font=("cambria", 18, "bold"), bg="gray90" ,compound=TOP,justify=LEFT ,width=100, height=100)
        label.pack(pady=100)


        self.win.mainloop()


C1=clas()