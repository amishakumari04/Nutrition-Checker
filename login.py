from tkinter import *  
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from menu1 import diet as diet   
                

from signin import signUp as sUp

def login_page():

    a = Tk() 
    a.title('Nutrition Checker- login')

    def Login1():   
        username=user_entry.get()
        if(user_entry.get() == "" or password_entry.get()==""):
            MessageBox.showinfo("ALERT","Username and password is required for login !")
        else:
            con = mysql.connect(host="localhost", user="root", password="password", database="diet")
            cursor = con.cursor()
            # cursor.execute("SELECT * FROM user_info WHERE USERNAME='"+user_entry.get()+"' and PASSWORD='"+password_entry.get()+"'")
            # db=cursor.fetchall()
            # result= cursor.rowcount
            # result= cursor.fetchone() 
            # MessageBox.showinfo("ALERT",cursor.rowcount)
            cursor.execute("SELECT USERNAME FROM user_info")
            database_user=cursor.fetchall()
            cursor.execute("SELECT PASSWORD FROM user_info")
            database_pass=cursor.fetchall()

            var1=0
            var2=0

            for USERNAME in database_user:
               user=USERNAME[0]
               u=str(user)
               if(u==user_entry.get()):
                   var1=1    
            for PASSWORD in database_pass:
               pas=PASSWORD[0]
               if(pas==password_entry.get()):
                   var2=1  

            if (var1==1 and var2==1):
                 a.destroy()
                 diet(username)
      
            else:
                MessageBox.showinfo("ALERT","Invalid Username or password!!")
  
            con.close();    

    def Signin():
         a.destroy()
         sUp()
    


    frame1 = Frame(master=a,width=133,height=1080,bg="#ff0000")
    frame1.pack(fill=Y, side=LEFT)

    frame3 = Frame(master=a, width=133, bg="#ff0000")
    frame3.pack(fill=Y, side=RIGHT)

    frame4 = Frame(master=a,width=133,bg="#fd5c63")
    frame4.pack(fill=Y, side=LEFT)

    frame5 = Frame(master=a, width=133, bg="#fd5c63")
    frame5.pack(fill=Y, side=RIGHT)

    frame6 = Frame(master=a,width=133,bg="#FBCEB1")
    frame6.pack(fill=Y, side=LEFT)

    frame7 = Frame(master=a, width=133, bg="#FBCEB1")
    frame7.pack(fill=Y, side=RIGHT)


    frame2 = Frame(master=a, width=1121)
    

    user=Label(frame2,text="Username:",font=("Calibre 12"))
    user.place(x=185,y=250)
    user_entry=Entry(frame2,font=("Calibre 12"))
    user_entry.place(x=310,y=250)
   
    password=Label(frame2,text="Password:",font=("Calibre 12"))
    password.place(x=185,y=300)
    password_entry=Entry(frame2,font=("Calibre 12"),show="*")
    password_entry.place(x=310,y=300)

    login1= Button(frame2, text="Log In",bg="black",fg="white" ,font=("Calibre 12"),command=Login1)
    login1.place(x=350,y=360)

    l1=Label(frame2,text="Do not have an account ?",fg="blue",font=("Calibre 10"))
    l1.place(x=185,y=430)

    create=Button(frame2,text="Sign Up",bg="black",fg="white" ,font=("Calibre 10"),command=Signin)
    create.place(x=350,y=430)

    exit=Button(frame2,text="Exit",bg="red",font=("Calibre 10"),command=a.destroy)
    exit.place(x=600,y=700)

    frame2.pack(fill=Y,side=TOP,expand=True)

    a.mainloop()
