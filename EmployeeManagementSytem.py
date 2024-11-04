from tkinter import *
import ttkthemes 
import time
from tkinter import ttk,filedialog
from tkinter import messagebox
import pandas
import pymysql


#Exit Button Functionality:--
def toexit():
   result = messagebox.askyesno('Confirm','Do you want to Exit?')
   if result:
      root.destroy()
   else:
      pass
   
#Export Button Functionality:--
def exportButton():
   url = filedialog.asksaveasfilename(defaultextension='.csv')
   index = StudentTable.get_children()
   newlist=[]
   for idx in index:
      content = StudentTable.item(idx)
      datalist = content['values']
      newlist.append(datalist)
   table = pandas.DataFrame(newlist,columns=['EmployeeId','Name','Email','MobileNo','Addess','gender','dob','Entrydate','Entrytime'])
   table.to_csv(url,index=FALSE)
   messagebox.showinfo('Success','Data is Saved Successfully')

def toplevelData(title,button_text,command):
   global identry,nameentry,emailentry,addressentry,mobileentry,genderentry,dobentry,screen
   screen = Toplevel()
   screen.resizable(0,0)
   screen.title(title)
   screen.grab_set()
   idlabel = Label(screen,text='Id',font=('Monospace','15','bold'))
   idlabel.grid(row=0,column=0,padx=10,pady=10,sticky=W)
   identry = Entry(screen,font=('Monospace','15','bold'),width=24)
   identry.grid(row=0,column=1,padx=10,pady=10)

   namelabel = Label(screen,text='Name',font=('Monospace','15','bold'))
   namelabel.grid(row=1,column=0,padx=10,pady=10,sticky=W)
   nameentry = Entry(screen,font=('Monospace','15','bold'),width=24)
   nameentry.grid(row=1,column=1,padx=10,pady=10)

   emaillabel = Label(screen,text='Email',font=('Monospace','15','bold'))
   emaillabel.grid(row=2,column=0,padx=10,pady=10,sticky=W)
   emailentry = Entry(screen,font=('Monospace','15','bold'),width=24)
   emailentry.grid(row=2,column=1,padx=10,pady=10)

   mobilelabel = Label(screen,text='Mobile No.',font=('Monospace','15','bold'))
   mobilelabel.grid(row=3,column=0,padx=10,pady=10,sticky=W)
   mobileentry = Entry(screen,font=('Monospace','15','bold'),width=24)
   mobileentry.grid(row=3,column=1,padx=10,pady=10)

   addresslabel = Label(screen,text='Address',font=('Monospace','15','bold'))
   addresslabel.grid(row=4,column=0,padx=10,pady=10,sticky=W)
   addressentry = Entry(screen,font=('Monospace','15','bold'),width=24)
   addressentry.grid(row=4,column=1,padx=10,pady=10)

   genderlabel = Label(screen,text='Gender',font=('Monospace','15','bold'))
   genderlabel.grid(row=5,column=0,padx=10,pady=10,sticky=W)
   genderentry = Entry(screen,font=('Monospace','15','bold'),width=24)
   genderentry.grid(row=5,column=1,padx=10,pady=10)

   doblabel = Label(screen,text='D.O.B',font=('Monospace','15','bold'))
   doblabel.grid(row=6,column=0,padx=10,pady=10,sticky=W)
   dobentry = Entry(screen,font=('Monospace','15','bold'),width=24)
   dobentry.grid(row=6,column=1,padx=10,pady=10)

   studentButton = ttk.Button(screen,text=button_text,command=command)
   studentButton.grid(row=7,column=0,columnspan=2,padx=10,pady=10)

   if button_text=='Update':
      index = StudentTable.focus()
      content = StudentTable.item(index)
      listdata = content['values']
      identry.insert(0,listdata[0])
      nameentry.insert(0,listdata[1])
      emailentry.insert(0,listdata[2])
      mobileentry.insert(0,listdata[3])
      addressentry.insert(0,listdata[4])
      genderentry.insert(0,listdata[5])
      dobentry.insert(0,listdata[6])
   
#Update student Button Functionality:--
def updateData():
   currentdate = time.strftime('%d/%m/%Y')
   currentTime = time.strftime('%H:%M:%S')
   query = 'update Employee set EmployeeId=%s,name=%s,Email=%s,MobileNo=%s,Address=%s,gender=%s,dob=%s,Entrydate=%s,Entrytime=%s where EmployeeId=%s'
   mycursor.execute(query,(identry.get(),nameentry.get(),emailentry.get(),mobileentry.get(),addressentry.get(),genderentry.get(),dobentry.get(),currentdate,currentTime,identry.get()))
   con.commit()
   messagebox.showinfo('Success',f'Id {identry.get()} is Modified.',parent = screen)
   screen.destroy()
   showstudent()
   


#Show student Button Functionality:--
def showstudent():
   query = 'select * from Employee'
   mycursor.execute(query)
   fetched_data = mycursor.fetchall()
   StudentTable.delete(*StudentTable.get_children())
   for data in fetched_data:
      datalist = list(data)
      StudentTable.insert('',END,values=datalist)

#Delete student Button Functionality:--
def deletestudent():
   index = StudentTable.focus()
   content = StudentTable.item(index)
   content_id = content['values'][0]
   query = 'delete from Employee where EmployeeId = %s'
   mycursor.execute(query,content_id)
   con.commit()
   messagebox.showinfo('Deleted',f'id {content_id} is Deleted Successfully.')
   query = 'select * from Employee'
   mycursor.execute(query)
   fetched_data = mycursor.fetchall()
   StudentTable.delete(*StudentTable.get_children())
   for data in fetched_data:
      datalist = list(data)
      StudentTable.insert('',END,values=datalist)

#Search student Button Functionality:--

def searchData():
   query = 'select * from Employee where EmployeeId=%s or name=%s or Email=%s or  MobileNo=%s or Address=%s or gender=%s or dob=%s'
   mycursor.execute(query,(identry.get(),nameentry.get(),emailentry.get(),mobileentry.get(),addressentry.get(),genderentry.get(),dobentry.get()))
   fetched_data = mycursor.fetchall()
   StudentTable.delete(*StudentTable.get_children())
   for data in fetched_data:
      StudentTable.insert('',END,values=data)

    
# Add student Button Functionality:--

def addData():
   if identry.get() == '' or nameentry.get() == '' or emailentry.get() == '' or mobileentry.get() == '' or addressentry.get() == '' or genderentry.get() == '' or dobentry.get() == '' :
      messagebox.showerror('Error','All Fields are Required',parent=screen)
   else:
      date = time.strftime('%d/%m/%Y')
      currentTime = time.strftime('%H:%M:%S')
      try:
         query = 'insert into Employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
         mycursor.execute(query,(identry.get(),nameentry.get(),emailentry.get(),mobileentry.get(),addressentry.get(),genderentry.get(),dobentry.get(),date,currentTime))
         con.commit()
         result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?')
         if result:
            identry.delete(0,END)
            nameentry.delete(0,END)
            emailentry.delete(0,END)
            mobileentry.delete(0,END)
            addressentry.delete(0,END)
            genderentry.delete(0,END)
            dobentry.delete(0,END)
         else:
            pass
      except:
         messagebox.showerror('Error','Id cannot be Duplicate',parent=screen)
         return 
      query = 'select * from Employee'
      mycursor.execute(query)
      fetched_data = mycursor.fetchall()
      StudentTable.delete(*StudentTable.get_children())
      for data in fetched_data:
         datalist = list(data)
         StudentTable.insert('',END,values=datalist)

#Clock && Date Functionality:--
def clockFunction():
   date = time.strftime('%d/%m/%Y')
   currentTime = time.strftime('%H:%M:%S')
   datetimelabel.config(text=f'     Date: {date} \n Time: {currentTime}')
   datetimelabel.after(1000,clockFunction)
      
#Connect Database Functionality:--
def connect_database():
   def connect():
      global mycursor,con
      try:
         con=pymysql.connect(host='localhost',user='root',password='Pawan@4961')
         mycursor = con.cursor()
      except:
         messagebox.showerror('Error','Invalid Detils',parent=connectWindow)
         return
      
      try:
         query = 'create database employeemanagementsystem'
         mycursor.execute(query)
         query = 'use employeemanagementsystem'
         mycursor.execute(query)
         query = 'create table Employee(EmployeeId int not null primary key, name varchar(50), Email varchar(50), MobileNo varchar(10), Address varchar(20), gender varchar(20), dob varchar(20) , Entrydate varchar(50) , Entrytime varchar(50))'
         mycursor.execute(query)
      except:
         query = 'use employeemanagementsystem'
         mycursor.execute(query)
      messagebox.showinfo('Success','Database Connection is Successful',parent=connectWindow)
      connectWindow.destroy()
      addstudentButton.config(state=NORMAL)
      searchstudentButton.config(state=NORMAL)
      deletestudentButton.config(state=NORMAL)
      updatestudentButton.config(state=NORMAL)
      showstudentButton.config(state=NORMAL)
      exportstudentButton.config(state=NORMAL)


   connectWindow = Toplevel()
   connectWindow.grab_set()
   connectWindow.geometry('470x250+730+230')
   connectWindow.title('Connecting Database...')
   connectWindow.resizable(0,0)

   hostnamelabel = Label(connectWindow,text='Hostname:',font=('Monospace','15','bold'))
   hostnamelabel.grid(row=0,column=0,padx=10,pady=10)
   hostnameEntry = Entry(connectWindow,font=('Monospace','15','bold'),width=25)
   hostnameEntry.grid(row=0,column=1,padx=8,pady=10)

   usernamelabel = Label(connectWindow,text='Username:',font=('Monospace','15','bold'))
   usernamelabel.grid(row=1,column=0,padx=10,pady=10)
   usernameEntry = Entry(connectWindow,font=('Monospace','15','bold'),width=25)
   usernameEntry.grid(row=1,column=1,padx=8,pady=10)

   passwordlabel = Label(connectWindow,text='Password:',font=('Monospace','15','bold'))
   passwordlabel.grid(row=2,column=0,padx=10,pady=10)
   passwordEntry = Entry(connectWindow,font=('Monospace','15','bold'),width=25)
   passwordEntry.grid(row=2,column=1,padx=8,pady=10)

   ConnectButton = ttk.Button(connectWindow,text='Connect',width=18,command=connect)
   ConnectButton.grid(row=3,columnspan=2,padx=10,pady=10)



root = ttkthemes.ThemedTk()
root.get_themes
root.set_theme('radiance')

#To Give Size to Window
root.geometry('1520x780+0+0')
root.resizable(FALSE,FALSE)
root.title("Employee Management System")

#Add Background image:--
# MainBackgroundimage = PhotoImage(file='green.png')
# MainBackgroundimagelabel = Label(root,image=MainBackgroundimage)
# MainBackgroundimagelabel.place(x=0,y=0)

#DateTime Label:--
datetimelabel = Label(root,font=('Monospace','14','bold'))
datetimelabel.place(x=5,y=5)
clockFunction()

#Student Management System Label:--
HeadingLabel = Label(root,text="Employee Management System",font=('Monospace','30','bold')) 
HeadingLabel.place(x=460,y=5)

#Connect Database Button:--
ConnectDatabaseButton = ttk.Button(root,text='Connect To Database',width=20,command=connect_database)
ConnectDatabaseButton.place(x=1300,y=20)

#Left Frame:--
Leftframe = Frame(root)
Leftframe.place(x=25,y=78,width=200,height=650)

Leftframeimage = PhotoImage(file='student.png')
LeftframeimageLabel = Label(Leftframe,image=Leftframeimage)
LeftframeimageLabel.grid(row=0,column=0,columnspan=2)

addstudentButton = ttk.Button(Leftframe,text='Add Employee',width=20,state=DISABLED,command=lambda:toplevelData('Add Employee','Add Employee',addData))
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton = ttk.Button(Leftframe,text='Search Employee',width=20,state=DISABLED,command=lambda:toplevelData('Search Employee','Search',searchData))
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton = ttk.Button(Leftframe,text='Delete Employee',width=20,state=DISABLED,command=deletestudent)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton = ttk.Button(Leftframe,text='Update Employee',width=20,state=DISABLED,command=lambda:toplevelData('Update Employee','Update',updateData))
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton = ttk.Button(Leftframe,text='Show Employee',width=20,state=DISABLED,command=showstudent)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton = ttk.Button(Leftframe,text='Export Data',width=20,state=DISABLED,command=exportButton)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton = ttk.Button(Leftframe,text='Exit',width=20,command=toexit)
exitButton.grid(row=7,column=0,pady=20,columnspan=2)


#Right Farme:-
Rightframe = Frame(root)
Rightframe.place(x=250,y=78,width=1245,height=650)

ScrollbarX = Scrollbar(Rightframe,orient=HORIZONTAL)
ScrollbarY = Scrollbar(Rightframe,orient=VERTICAL)
ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)

StudentTable = ttk.Treeview(Rightframe,columns=('EmployeeId','Name','Email','Mobile No.','Address','Gender','D.O.B','Entry Date','Entry Time'),xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)

ScrollbarX.config(command=StudentTable.xview)
ScrollbarY.config(command=StudentTable.yview)

StudentTable.pack(fill=BOTH,expand=1)
StudentTable.heading('EmployeeId',text='Id')
StudentTable.heading('Name',text='Name')
StudentTable.heading('Email',text='Email')
StudentTable.heading('Mobile No.',text='Mobile No.')
StudentTable.heading('Address',text='Address')
StudentTable.heading('Gender',text='Gender')
StudentTable.heading('D.O.B',text='D.0.B')
StudentTable.heading('Entry Date',text='Entry Date')
StudentTable.heading('Entry Time',text='Entry Time')


StudentTable.column('EmployeeId',width=60,anchor=CENTER)
StudentTable.column('Name',width=300,anchor=CENTER)
StudentTable.column('Email',width=300,anchor=CENTER)
StudentTable.column('Mobile No.',width=150,anchor=CENTER)
StudentTable.column('Address',width=150,anchor=CENTER)
StudentTable.column('Gender',width=110,anchor=CENTER)
StudentTable.column('D.O.B',width=155,anchor=CENTER)
StudentTable.column('Entry Date',width=200,anchor=CENTER)
StudentTable.column('Entry Time',width=200,anchor=CENTER)
style = ttk.Style()
style.configure('Treeview',rowheight=30,font=('Monospace','10','bold'),foreground='black')
style.configure('Treeview.Heading',font=('Monospace','12','bold'),foreground='black')

StudentTable.config(show='headings')
root.mainloop()