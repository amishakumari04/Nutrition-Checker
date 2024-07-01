from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import login
import menu1


def profile1(username):
   
   x=Tk()
   x.title("Nutrition Checker-Profile")
   x.geometry("1920x1080")

   def close():
      x.destroy()
      menu1.diet(username)

   def show(username):

      con = mysql.connect(host="localhost", user="root", password="Amisha@123", database="diet",auth_plugin='mysql_native_password')
      cursor = con.cursor()
      cursor.execute("select * from user_info where USERNAME= '"+username +"'")
      rows = cursor.fetchall()
  
      for row in rows:
         fname1_entry.insert(0, row[0])
         contact1_entry.insert(0, row[1])
         email1_entry.insert(0,row[2])
         gender1_entry.insert(0,row[3])
         weight1_entry.insert(0,row[4])
         height1_entry.insert(0,row[5])
         user_entry.insert(0,row[6])
         password_entry.insert(0,row[7])
  
      con.close();

   def update( ):
    fname = fname1_entry.get()
    contact= contact1_entry.get()
    email =email1_entry.get()
    gender=gender1_entry.get()
    height=height1_entry.get()
    weight=weight1_entry.get()


  
    if(fname == "" or contact == "" or email==""):
        MessageBox.showinfo("ALERT", "These fields are required to update!")
    else:
        con = mysql.connect(host="localhost", user="root", password="Amisha@123", database="diet")
        cursor = con.cursor()
        cursor.execute("update user_info set FIRSTNAME = '"+ fname +"', CONTACT='"+ contact +"',EMAIL='"+email+"',GENDER='"+gender+"',WEIGHT='"+weight+"',HEIGHT='"+height+"' where USERNAME ='"+ username +"'")
        cursor.execute("commit");
  
        MessageBox.showinfo("Status", "Account successfully Updated")
        con.close();
   
   def delete():
        con = mysql.connect(host="localhost", user="root", password="Amisha@123", database="diet")
        cursor = con.cursor()
        cursor.execute("delete from user_info where USERNAME='"+ username +"'")
        cursor.execute("commit");

        fname1_entry.delete(0, 'end')
        contact1_entry.delete(0, 'end')
        email1_entry.delete(0, 'end')
        height1_entry.delete(0, 'end')
        weight1_entry.delete(0, 'end')
        gender1_entry.delete(0, 'end')
        user_entry.delete(0,'end')
        password_entry.delete(0,'end')
  
        MessageBox.showinfo("Status", "Account successfully Deleted")
        con.close();
        x.destroy()
        login.login_page()

   f1=Frame(x,bg="black",width=125,height=1080).place(x=1440,y=0)
   f2=Frame(x,bg="light blue",width=125,height=1080).place(x=1320,y=0)
   f3=Frame(x,bg="#A7C7E7",width=125,height=1080).place(x=1200,y=0)
   f4=Frame(x,bg="light green",width=125,height=1080).place(x=1080,y=0)
   f5=Frame(x,bg="#FDFD96",width=155,height=1080).place(x=0,y=0)
   fr=Frame(x,width=705,height=1080)

   fname=Label(fr,text="Full name: *",font=("Calibre 15")).grid(row=0,column=0,sticky=E,pady=15)
   fname1_entry=Entry(fr,font=("Calire 15"))
   fname1_entry.grid(row=0,column=1,pady=15,padx=2,sticky=W)

   contact=Label(fr,text="Contact no. : *",font=("Calibre 15")).grid(row=1,column=0,sticky=E,pady=15)
   contact1_entry=Entry(fr,font=("Calibre 15"))
   contact1_entry.grid(row=1,column=1,pady=15,padx=2,sticky=W)

   email=Label(fr,text="E.maid id : *",font=("Calibre 15")).grid(row=2,column=0,sticky=E,pady=15)
   email1_entry=Entry(fr,font=("Calibre 15"))
   email1_entry.grid(row=2,column=1,pady=15,padx=2)

   gender=Label(fr,text="Gender:",font=("Calibre 15")).grid(row=3,column=0,sticky=E,pady=15)
   gender1_entry=Entry(fr,font=("Calire 15"))
   gender1_entry.grid(row=3,column=1,pady=15,padx=2,sticky=W)

   weight=Label(fr,text="Weight(in kg) :",font=("Calibre 15")).grid(row=4,column=0,sticky=E,pady=15)
   weight1_entry=Entry(fr,font=("Calibre 15"))
   weight1_entry.grid(row=4,column=1,pady=15,padx=2,sticky=W)
   height=Label(fr,text="Height(in cm) :",font=("Calibre 15")).grid(row=5,column=0,sticky=E,pady=15)
   height1_entry=Entry(fr,font=("Calibre 15"))
   height1_entry.grid(row=5,column=1,pady=15,padx=2,sticky=W)

   user=Label(fr,text="Username :",font=("Calibre 15")).grid(row=6,column=0,sticky=E,pady=15)
   user_entry=Entry(fr,font=("Calibre 15"))
   user_entry.grid(row=6,column=1,pady=15,padx=2,sticky=W)

   password=Label(fr,text="Password :",font=("Calibre 15")).grid(row=7,column=0,sticky=E,pady=15)
   password_entry=Entry(fr,font=("Calibre 15"))
   password_entry.grid(row=7,column=1,pady=15,padx=2,sticky=W)

   l7=Label(fr,text=" ",font=("Calibre 15"))
   l7.grid(row=8,column=4,sticky=E,pady=15)

   show(username)

   updatebtn=Button(fr,text="Update",font=("Calibre 15"),bg="blue",fg="white",command=update)
   updatebtn.grid(row=9,column=1,sticky=NW)
   deletebtn=Button(fr,text="Delete",font=("Calibre 15"),bg="blue",fg="white",command=delete)
   deletebtn.grid(row=9,column=1,sticky=NE)
   closebtn=Button(fr,text="Close",font=("Calibre 15"),bg="green",fg="white",command=close)
   closebtn.grid(row=10,column=1,sticky=SE)

   fr.place(x=155,y=0)

   x.mainloop()

