from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == "admin" and passwordEntry.get() == "admin":
        messagebox.showinfo("Success", "Welcome")
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error', 'Invalid username or password')


window = Tk()

window.geometry("1280x700+0+0")
window.title("Student Management System")
window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='background.jpg')
bgLabel = Label(window, image=backgroundImage)
bgLabel.place(y=0, x=0)

loginFrame = Frame(window, bg='white')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, pady=10, columnspan=2)

usernameImage = PhotoImage(file="user.png")
usernameLabel = Label(loginFrame, image=usernameImage, text="Username", compound=LEFT,
                      font=("times new roman", 20, 'bold'), bg='white')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

usernameEntry = Entry(loginFrame, font=("times new roman", 20, 'bold'))
usernameEntry.grid(row=1, column=1, padx=10)

passwordImage = PhotoImage(file="password.png")
passwordLabel = Label(loginFrame, image=passwordImage, text="Password", compound=LEFT,
                      font=("times new roman", 20, 'bold'), bg='white')
passwordLabel.grid(row=2, column=0, pady=10, padx=20)

passwordEntry = Entry(loginFrame, font=("times new roman", 20, 'bold'))
passwordEntry.grid(row=2, column=1, padx=10)

loginButton = Button(loginFrame, text='Login', font=("times new roman", 20, 'bold'), width=15, fg='blue', bg='white',
                     activebackground='blue', activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=30)

window.mainloop()
