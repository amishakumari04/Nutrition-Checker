from tkinter import *  
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import login


def signUp():
   b = Tk() 
   b.title('Nutrition Checker- Sign In')
   b.geometry("1920x1080")


   def create():
     fname = fname_entry.get()
     contact= contact_entry.get()
     email= email_entry.get()
     gender=gender_entry.get()
     weight=weight_entry.get()
     height=height_entry.get()
     user=user_entry.get()
     password=password_entry.get()
  
     if(fname == "" or contact == "" or email == "" or user=="" or password==""):
         MessageBox.showinfo("ALERT", "Please enter all required(*) fields")
     else:
         con = mysql.connect(host="localhost", user="root", password="Amisha@123", database="diet")
         cursor = con.cursor()
         cursor.execute("INSERT INTO user_info VALUES ('"+fname+"','"+contact+"','"+email+"','"+gender+"','"+weight+"','"+height+"','"+user+"','"+password+"')")
        #  ('FIRST NAME', 'CONTACT', 'EMAIL', 'GENDER', 'WEIGHT', 'HEIGHT', 'USERNAME', 'PASSWORD')
         cursor.execute("commit")
         con.close();
         MessageBox.showinfo("Status", "Account created successfully")
         b.destroy()
         login.login_page()

   frame1 = Frame(master=b,height=200,width=400,bg="lightblue").place(x=0,y=0)
   frame2 = Frame(master=b,height=200,width=400,bg="grey").place(x=0,y=200)
   frame3 = Frame(master=b,height=200,width=400,bg="lightblue").place(x=0,y=400)
   frame4 = Frame(master=b,height=200,width=400,bg="grey").place(x=0,y=600)
   f=Frame(b,width=1520,height=1080)
   f.place(x=400,y=0)

   extra=Label(f,text="")
   extra.grid(row=0,column=0)

   fname=Label(f,text="Full name: *")
   fname.grid(row=0,column=6,sticky=E,pady=30)
   fname_entry=Entry(f)
   fname_entry.grid(row=0,column=7,pady=3,padx=2,sticky=W)

   contact=Label(f,text="Contact no. : *")
   contact.grid(row=1,column=6,sticky=E,pady=10)
   contact_entry=Entry(f)
   contact_entry.grid(row=1,column=7,pady=3,padx=2,sticky=W)

   email=Label(f,text="E.maid id : *")
   email.grid(row=2,column=6,sticky=E,pady=10)
   email_entry=Entry(f)
   email_entry.grid(row=2,column=7,pady=3,padx=2,sticky=W)

   lx=Label(f,text="(SOME PERSONAL DATA)",fg="blue")
   lx.grid(row=3,column=6,sticky=E,pady=10)
   gender=Label(f,text="Gender:")
   gender.grid(row=4,column=6,sticky=E,pady=10)
   gender_entry=Entry(f)
   gender_entry.grid(row=4,column=7,pady=3,padx=2,sticky=W)
   # r1=Radiobutton(f,text="Male",variable=v,value=1).grid(row=4,column=1,pady=10)
   # r2=Radiobutton(f,text="Female",variable=v,value=2).grid(row=4,column=2,pady=10)

   weight=Label(f,text="Weight(in kg) :")
   weight.grid(row=5,column=6,sticky=E,pady=10)
   weight_entry=Entry(f)
   weight_entry.grid(row=5,column=7,pady=3,padx=2,sticky=W)

   height=Label(f,text="Height(in cm) :")
   height.grid(row=6,column=6,sticky=E,pady=10)
   height_entry=Entry(f)
   height_entry.grid(row=6,column=7,pady=3,padx=2,sticky=W)

   l7=Label(f,text=" ")
   l7.grid(row=7,column=6,sticky=E,pady=10)

   l8=Label(f,text="(REMEMBER THE USERNAME AND PASSWORDS FOR FURTHER LOGINS) ",fg="blue")
   l8.grid(row=8,column=6,columnspan=2,sticky=E,pady=10)

   user=Label(f,text="Username: *")
   user.grid(row=9,column=6)
   user_entry=Entry(f)
   user_entry.grid(row=9,column=7)

   password=Label(f,text="Password: *")
   password.grid(row=10,column=6)
   password_entry=Entry(f,show="*")
   password_entry.grid(row=10,column=7)

   l9=Label(f,text="")
   l9.grid(row=10,column=0,sticky=W,pady=10)


   create=Button(f,text="Create Account",bg="yellow",command=create)
   create.grid(row=11,column=8)

   b.mainloop()

  