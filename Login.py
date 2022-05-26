from tkinter import *
import HomePage
from PIL import ImageTk
import tkinter.messagebox as mymessagebox
import pyodbc
import Register




class Log():
    def __init__(self):

        #window

        #bg=ImageTk.PhotoImage(file=r"""E:\SSD\Uni\Graduation Project\GUI\brain1.jpg""")
        self.tkWindow = Tk()

        self.tkWindow.geometry('925x500+300+200')
        self.tkWindow.resizable(False,False)
        self.tkWindow.iconbitmap(r"""E:\SSD\Uni\Graduation Project\GUI\download.ico""")
        self.tkWindow.title('LOGIN')
        #tkWindow.configure(background='#F2F2F2')
        self.tkWindow.configure(background='white')


        #______brain tumor classifier text
        BTC=Label(text="Brain tumor classifier",fg="#8B3A3A",font=("cambria",30,"bold"),bg="white").place(x=470,y=50)
        BTC = StringVar()

        bg=ImageTk.PhotoImage(file=r"""E:\SSD\Uni\Graduation Project\Images\Brain-Tumor-1152219092-696x557.png""")
        bg_image=Label(self.tkWindow,image=bg,border=0).place(x=470,y=100)


        #LoginLabel= Label(tkWindow , text= "Login" , font=myFont).grid(row=0 , column=5)
        Frame_login = Frame(self.tkWindow, bg="white")
        Frame_login.place(x=0, y=0, height=550, width=400)
        title = Label(Frame_login, text="Login", font=("cambria", 35, "bold"), bg="white").place(x=120, y=30)



        def on_enter(e):
            usernameEntry.delete(0, 'end')


        def on_leave(e):
            if usernameEntry.get() == '':
                usernameEntry.insert(0, 'Username')

        self.username = StringVar()
        usernameEntry = Entry(Frame_login, fg='black',bg='white', textvariable=self.username, border=0, font=("times new roman", 15))
        usernameEntry.place(x=30, y=120, width=350, height=35)
        usernameEntry.insert(0, 'Username')
        usernameEntry.bind("<FocusIn>", on_enter)
        usernameEntry.bind("<FocusOut>", on_leave)
        Frame(Frame_login, width=330, height=2, bg='gray50').place(x=30, y=160)


        def oon_enter(e):
            passwordEntry.delete(0, 'end')
            passwordEntry.config(show='*')



        def oon_leave(e):
            if passwordEntry.get() == '':
                passwordEntry.insert(0, 'Password')
                passwordEntry.config(show='')

        self.password = StringVar()
        passwordEntry = Entry(Frame_login, border=0, textvariable=self.password, font=("times new roman", 15), bg="gray100")
        passwordEntry.place(x=30, y=200, width=350, height=35)
        passwordEntry.insert(0,'Password')
        passwordEntry.bind("<FocusIn>", oon_enter)
        passwordEntry.bind("<FocusOut>", oon_leave)
        Frame(Frame_login, width=330, height=2, bg='gray50').place(x=30, y=240)






        login_button=Button(Frame_login,text="Login",width=27,pady=7,bg="#57a1f8",fg='white',border=0,command=self.validateLogin,font=("cambria",15,"bold")).place(x=30,y=300)
        self.tkWindow.bind('<Return>',self.validateLogin)




        #Register_button=Button(Frame_login,text="Register",command=lambda:[tkWindow.destroy(),Register.RG()],bg="gray90",font=("cambria",15,"bold")).place(x=140,y=350)
        Register_button=Button(Frame_login,text="Register",width=27,border=0,pady=7,bg="#595959",fg='white',command=lambda:[self.tkWindow.destroy(),Register.RG()],font=("cambria",15,"bold")).place(x=30,y=370)
        #tkWindow.configure(background='#54596d')

        self.tkWindow.mainloop()


    def validateLogin(self,*event):


        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=KIMOO\SQLEXPRESS;'
                              'Database=BTD;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM LOGg where username = '" + self.username.get() + "' and password = '" + self.password.get() + "';")
        myresult = cursor.fetchone()
        if myresult == None:
            mymessagebox.showerror("Error", "Invalid User Name or Password")

        else:

             self.tkWindow.destroy()
             HomePage.HP()
             conn.close()
             cursor.close()



#LG=Log()




