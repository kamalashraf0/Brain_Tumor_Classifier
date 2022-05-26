import pyodbc
import tkinter.messagebox as mymessagebox
from tkinter import*



root = Tk()
root.geometry('400x500')
root.title("Registration Form")
label_0 = Label(root, text="Register", font=("cambria", 35, "bold")).place(x=110, y=30)





#username label and text entry box
lbl_user=Label(root,text="Username",font=("cambria",15,"bold"),bg="gray90").place(x=30,y=130)
username = StringVar()
usernameEntry = Entry(root, textvariable=username,font=("times new roman",15),bg="gray100")
usernameEntry.place(x=30,y=170,width=350,height=35)

#password label and password entry box
lbl_pass = Label(root, text="Password", font=("cambria", 15, "bold"), bg="gray90").place(x=30, y=230)
password = StringVar()
passwordEntry = Entry(root, textvariable=password,  font=("times new roman", 15), bg="gray100",show='*')
passwordEntry.place(x=30, y=270, width=350, height=35)
conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=KIMOO\SQLEXPRESS;'
                              'Database=BTD;'
                              'Trusted_Connection=yes;')

cursor = conn.cursor()
command=cursor.execute("INSERT INTO LOGg (username,password) VALUES (%s,$s)",[username.get(),username.get()])
cursor.commit()

#mymessagebox.showinfo("Success", "Sign UP Successfully")

#root.destroy()
# conn.close()
# cursor.close()


SignUP_button=Button(root,text="Sign Up",bg="gray90",command=command,font=("cambria",15,"bold")).place(x=30,y=350)
root.mainloop()