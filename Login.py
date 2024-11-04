from tkinter import *
from tkinter import messagebox

window = Tk()

#Login Button Functionality:--
def Login():
    if UsernameEntry.get() == '' or PasswordEntry.get == '':
        messagebox.showerror('Error','Fields cannot be empty.')
    elif UsernameEntry.get() == 'Pawan' and PasswordEntry.get() == '1234':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import EmployeeManagementSytem
    else:
        messagebox.showerror('Error','Please Enter Correct Credentials')


####----GUI----####   
#To Give Size to Window
window.geometry('1200x700+150+40')
window.resizable(FALSE,FALSE)
window.title('Login System of Employee Management System')

#Adding Background image in Login Page
background_Login_image = PhotoImage(file ='Background.png')
background_Login_image_label= Label(window,image=background_Login_image)
background_Login_image_label.place(x=0,y=0)

### Frames:- It's Container to store entry fields

#Create That Container:--
LoginFrame = Frame(window,bg='#2c4b82')
LoginFrame.place(x=700,y=150)

#UserLogo:--
UserLogoimage = PhotoImage(file='userLogo.png')
UserLogoimage_label = Label(LoginFrame,image=UserLogoimage,borderwidth=0)
UserLogoimage_label.grid(row=0,column=1,pady=15)

#Username Input Field:--
Usernameimagelogo = PhotoImage(file="user.png")
Username_Label = Label(LoginFrame,image=Usernameimagelogo,text='Username',compound=LEFT,font=('cambria','15','bold'),bg='#2c4b82')
Username_Label.grid(row=1,column=0,padx=15)
UsernameEntry = Entry(LoginFrame,font=('cambria','15','bold'),bd=2)
UsernameEntry.grid(row=1,column=1)

#Password Input Field:--
Passwordimagelogo = PhotoImage(file="Password.png")
Password_Label = Label(LoginFrame,image=Passwordimagelogo,text='Password',compound=LEFT,font=('cambria','15','bold'),bg='#2c4b82')
Password_Label.grid(row=2,column=0,padx=15,pady=10)
PasswordEntry = Entry(LoginFrame,font=('cambria','15','bold'),bd=2)
PasswordEntry.grid(row=2,column=1)

#LoginButton:--
LoginButton = Button(LoginFrame,text='Login',font=('cambria','13','bold'),bg='#8ed8d9',width=12,activebackground='#8ed8d9',activeforeground='black',cursor='hand2',command=Login)
LoginButton.grid(row=3,column=1,pady=20)


# To make Appear Window
window.mainloop()