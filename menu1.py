from tkinter import * 
from time import strftime 
import tkinter.messagebox as MessageBox
import webbrowser
import mysql.connector as mysql
from PIL import Image, ImageTk
import profile_edit
import login

def url():
      url=webbrowser.open_new("https://simple.wikipedia.org/wiki/Healthy_lifestyle")

    

def diet(username):
  
   root = Tk() 
   root.title('Nutrient Checker-Main window') 
   root.geometry("1920x1080")

   def pro():
    root.destroy()
    profile_edit.profile1(username)  

   calorie=0

   def add():
       calorie=calorie+int(cal_entry.get())

   def logout():
       root.destroy()
       login.login_page()
   

   def Select():
  
      if(food_entry.get() == ""):
          MessageBox.showinfo("ALERT","Food name is required to know the nutrient content!")
      else:
          con = mysql.connect(host="localhost", user="root", password="password", database="diet")
          cursor = con.cursor()
          cursor.execute("select * from food_chart where food= '" + food_entry.get() +"'")
          rows = cursor.fetchall()
  
          for row in rows:
              cal_entry.insert(0, row[1])
              pro_entry.insert(0, row[2])
              fat_entry.insert(0, row[3])
            #   calorie=calorie+row[1]

  
          con.close();
  
   menubar = Menu(root) 
   
   file = Menu(menubar, tearoff = 0) 
   menubar.add_cascade(label ='MENU', menu = file) 
   file.add_command(label ='Profle',command = pro)
  
   file.add_command(label ='Health tips', command = url) 

   file.add_separator() 
   file.add_command(label ='Logout', command =logout) 
   root.config(menu = menubar) 

   frame1 = Frame(master=root,width=400,height=1040,bg="pink")

#    image1 = ImageTk.PhotoImage(Image.open("fruits.png"))

#    image_label =Label(root, image=image1)
#    image_label.place(x=40,y=60)

#    image2 = ImageTk.PhotoImage(Image.open("balanced_diet.jpg"))

#    image2_label =Label(root, image=image2)
#    image2_label.place(x=40,y=400)


   frame1.pack(fill=Y, side=LEFT)
   


   frame3 = Frame(master=root, width=400, bg="grey")
   
   
#    image3 = ImageTk.PhotoImage(Image.open("yoga.jpg"))

#    image3_label =Label(frame3, image=image3)
#    image3_label.place(x=40,y=60)

   
#    image4 = ImageTk.PhotoImage(Image.open("gym.jpg"))

#    image4_label =Label(frame3, image=image4)
#    image4_label.place(x=40,y=400)

   frame3.pack(fill=Y, side=RIGHT)



   frame2 = Frame(master=root, width=1120)
   


   food=Label(frame2,text="Enter the name of the food whose nutrient contents you want to know",font=("verdana 12")).grid(row=0,column=0,sticky = E, pady = 35, padx=50)
   food_entry=Entry(frame2,font=("verdana 12"))
   food_entry.grid(row = 1, column = 0,columnspan=4 ,pady = 2, padx=2)

   btnSelect= Button(frame2, text="Search",bg="yellow" ,font=("verdana 12"),command=Select).grid(row=2,column=0,pady =30, padx=2)

   empty=Label(frame2,text="").grid(row=3,pady=40)

   cal = Label(frame2, text="Calories:", font=("Calibre 10")).place(x=40,y=250)
   cal_entry = Entry(frame2, font=("verdana 10"))
   cal_entry.place(x=140,y=250)
  
   protein= Label(frame2, text="Protien:", font=("Calibre 10")).place(x=40,y=290)
   pro_entry = Entry(frame2, font=("verdana 10"))
   pro_entry.place(x=140,y=290)
  
   fat = Label(frame2, text="Carbohydrates:", font=("Calibre 10")).place(x=40,y=340)
   fat_entry= Entry(frame2, font=("verdana 10"))
   fat_entry.place(x=140,y=340)

#    add=Label(frame2,text="Click add to maintain a daily calorie count.",font=("Calibre 10"))
#    add.place(x=40,y=420)
#    add_button=Button(frame2,text="Add",font=("Calibre 10"),bg="lightgreen",command=add)
#    add_button.place(x=300,y=420)

#    cal_count=Label(frame2,text="Calories consumed today :"+str(calorie),font=("Calibre 12"))
#    cal_count.place(x=140,y=480)

   frame2.pack(fill=Y,side=TOP,expand=True)
   root.mainloop()



