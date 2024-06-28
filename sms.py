from tkinter import *
import time

import pymysql
import ttkthemes
from tkinter import ttk, messagebox


# Functional section

def update():
    id= ''
    def updateQuery():
        print(
            "name " + nameEntry.get() + " mobile " + mobileEntry.get() + " email " + emailEntry.get() + " address " + addressEntry.get() + " gender " + genderEntry.get() + " dob " + dobEntry.get())

        if (
                nameEntry.get() == "" or mobileEntry.get() == "" or emailEntry.get() == "" or addressEntry.get() == "" or genderEntry.get() == ""):
            messagebox.showerror("Error", "All fields should be fill", parent=updateStudentWindow)
        else:
            query = "UPDATE `student` SET `name` = %s , mobile_no = %s , email = %s , address = %s , gender = %s , dob = %s WHERE `student`.`id` = %s;"

            myCursor.execute(query, (nameEntry.get(), mobileEntry.get(), emailEntry.get(),
                                     addressEntry.get(), genderEntry.get(), dobEntry.get(),id))
            con.commit()
            messagebox.showinfo("Confirm", "Data update successfully.")
            updateStudentWindow.destroy()
            show()

    updateStudentWindow = Toplevel()
    updateStudentWindow.grab_set()
    updateStudentWindow.resizable(0, 0)
    updateStudentWindow.geometry("400x400+100+100")

    idLabel = Label(updateStudentWindow, text="ID", font=('arial', '15', 'bold'))
    idLabel.grid(row=0, column=0, padx=10, pady=10)
    idEntry = Entry(updateStudentWindow, font=('arial', '15', 'bold'))
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    nameLabel = Label(updateStudentWindow, text="Name", font=('arial', '15', 'bold'))
    nameLabel.grid(row=1, column=0, padx=10, pady=10)
    nameEntry = Entry(updateStudentWindow, font=('arial', '15', 'bold'))
    nameEntry.grid(row=1, column=1, padx=10, pady=10)

    mobileLabel = Label(updateStudentWindow, text="Mobile No", font=('arial', '15', 'bold'))
    mobileLabel.grid(row=2, column=0, padx=10, pady=10)
    mobileEntry = Entry(updateStudentWindow, font=('arial', '15', 'bold'))
    mobileEntry.grid(row=2, column=1, padx=10, pady=10)

    emailLabel = Label(updateStudentWindow, text="Email", font=('arial', '15', 'bold'))
    emailLabel.grid(row=3, column=0, padx=10, pady=10)
    emailEntry = Entry(updateStudentWindow, font=('arial', '15', 'bold'))
    emailEntry.grid(row=3, column=1, padx=10, pady=10)

    addressLabel = Label(updateStudentWindow, text="Address", font=('arial', '15', 'bold'))
    addressLabel.grid(row=4, column=0, padx=10, pady=10)
    addressEntry = Entry(updateStudentWindow, font=('arial', '15', 'bold'))
    addressEntry.grid(row=4, column=1, padx=10, pady=10)

    genderLabel = Label(updateStudentWindow, text="Gender", font=('arial', '15', 'bold'))
    genderLabel.grid(row=5, column=0, padx=10, pady=10)
    genderEntry = Entry(updateStudentWindow, font=('arial', '15', 'bold'))
    genderEntry.grid(row=5, column=1, padx=10, pady=10)

    dobLabel = Label(updateStudentWindow, text="Date of Birth", font=('arial', '15', 'bold'))
    dobLabel.grid(row=6, column=0, padx=10, pady=10)
    dobEntry = Entry(updateStudentWindow, font=('arial', '15', 'bold'))
    dobEntry.grid(row=6, column=1, padx=10, pady=10)

    addStudentButton = ttk.Button(updateStudentWindow, text='Update',command=updateQuery)
    addStudentButton.grid(row=7, columnspan=2, padx=10, pady=10)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listData=content['values']
    print(listData)
    id=listData[0]
    idEntry.insert(0,listData[0])
    nameEntry.insert(0,listData[1])
    mobileEntry.insert(0,listData[2])
    emailEntry.insert(0,listData[3])
    addressEntry.insert(0,listData[4])
    genderEntry.insert(0,listData[5])
    dobEntry.insert(0,listData[6])


def show():
    query = "select * from student"
    myCursor.execute(query)
    fetchedData = myCursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetchedData:
        dataList = list(data)
        studentTable.insert('', END, values=dataList)

def addStudent():
    def add():
        print(
            "name " + nameEntry.get() + " mobile " + mobileEntry.get() + " email " + emailEntry.get() + " address " + addressEntry.get() + " gender " + genderEntry.get() + " dob " + dobEntry.get())

        if (
                nameEntry.get() == "" or mobileEntry.get() == "" or emailEntry.get() == "" or addressEntry.get() == "" or genderEntry.get() == ""):
            messagebox.showerror("Error", "All fields should be fill", parent=addStudentWindow)
        else:
            query = "INSERT INTO `student`( `name`, `mobile_no`, `email`, `address`, `gender`, `dob`, `added_date`, `added_time`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            date = time.strftime("%d/%m/%Y")
            currentTime = time.strftime("%H:%M:%S")
            myCursor.execute(query, (nameEntry.get(), mobileEntry.get(), emailEntry.get(),
                                     addressEntry.get(), genderEntry.get(), dobEntry.get(), date, currentTime))
            con.commit()
            result = messagebox.askyesno("Confirm", "Data added successfully. Do you want to clear this form?")
            if result:
                nameEntry.delete(0, END)
                mobileEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                genderEntry.delete(0, END)
                dobEntry.delete(0, END)
            else:
                pass

            show()

    addStudentWindow = Toplevel()
    addStudentWindow.grab_set()
    addStudentWindow.resizable(0, 0)
    addStudentWindow.geometry("400x400+100+100")

    nameLabel = Label(addStudentWindow, text="Name", font=('arial', '15', 'bold'))
    nameLabel.grid(row=0, column=0, padx=10, pady=10)
    nameEntry = Entry(addStudentWindow, font=('arial', '15', 'bold'))
    nameEntry.grid(row=0, column=1, padx=10, pady=10)

    mobileLabel = Label(addStudentWindow, text="Mobile No", font=('arial', '15', 'bold'))
    mobileLabel.grid(row=1, column=0, padx=10, pady=10)
    mobileEntry = Entry(addStudentWindow, font=('arial', '15', 'bold'))
    mobileEntry.grid(row=1, column=1, padx=10, pady=10)

    emailLabel = Label(addStudentWindow, text="Email", font=('arial', '15', 'bold'))
    emailLabel.grid(row=2, column=0, padx=10, pady=10)
    emailEntry = Entry(addStudentWindow, font=('arial', '15', 'bold'))
    emailEntry.grid(row=2, column=1, padx=10, pady=10)

    addressLabel = Label(addStudentWindow, text="Address", font=('arial', '15', 'bold'))
    addressLabel.grid(row=3, column=0, padx=10, pady=10)
    addressEntry = Entry(addStudentWindow, font=('arial', '15', 'bold'))
    addressEntry.grid(row=3, column=1, padx=10, pady=10)

    genderLabel = Label(addStudentWindow, text="Gender", font=('arial', '15', 'bold'))
    genderLabel.grid(row=4, column=0, padx=10, pady=10)
    genderEntry = Entry(addStudentWindow, font=('arial', '15', 'bold'))
    genderEntry.grid(row=4, column=1, padx=10, pady=10)

    dobLabel = Label(addStudentWindow, text="Date of Birth", font=('arial', '15', 'bold'))
    dobLabel.grid(row=5, column=0, padx=10, pady=10)
    dobEntry = Entry(addStudentWindow, font=('arial', '15', 'bold'))
    dobEntry.grid(row=5, column=1, padx=10, pady=10)

    addStudentButton = ttk.Button(addStudentWindow, text='Add Student', command=add)
    addStudentButton.grid(row=6, columnspan=2, padx=10, pady=10)

def searchStudent():
    def search():
        query = "select * from student where id=%s or name=%s or mobile_no=%s or email=%s or address=%s or gender=%s or dob=%s"
        myCursor.execute(query, (idEntry.get(),nameEntry.get(),mobileEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        fetchedData = myCursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetchedData:
            dataList = list(data)
            studentTable.insert('', END, values=dataList)

    searchStudentWindow = Toplevel()
    searchStudentWindow.grab_set()
    searchStudentWindow.resizable(0, 0)
    searchStudentWindow.geometry("400x400+100+100")

    idLabel = Label(searchStudentWindow, text="ID", font=('arial', '15', 'bold'))
    idLabel.grid(row=0, column=0, padx=10, pady=10)
    idEntry = Entry(searchStudentWindow, font=('arial', '15', 'bold'))
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    nameLabel = Label(searchStudentWindow, text="Name", font=('arial', '15', 'bold'))
    nameLabel.grid(row=1, column=0, padx=10, pady=10)
    nameEntry = Entry(searchStudentWindow, font=('arial', '15', 'bold'))
    nameEntry.grid(row=1, column=1, padx=10, pady=10)

    mobileLabel = Label(searchStudentWindow, text="Mobile No", font=('arial', '15', 'bold'))
    mobileLabel.grid(row=2, column=0, padx=10, pady=10)
    mobileEntry = Entry(searchStudentWindow, font=('arial', '15', 'bold'))
    mobileEntry.grid(row=2, column=1, padx=10, pady=10)

    emailLabel = Label(searchStudentWindow, text="Email", font=('arial', '15', 'bold'))
    emailLabel.grid(row=3, column=0, padx=10, pady=10)
    emailEntry = Entry(searchStudentWindow, font=('arial', '15', 'bold'))
    emailEntry.grid(row=3, column=1, padx=10, pady=10)

    addressLabel = Label(searchStudentWindow, text="Address", font=('arial', '15', 'bold'))
    addressLabel.grid(row=4, column=0, padx=10, pady=10)
    addressEntry = Entry(searchStudentWindow, font=('arial', '15', 'bold'))
    addressEntry.grid(row=4, column=1, padx=10, pady=10)

    genderLabel = Label(searchStudentWindow, text="Gender", font=('arial', '15', 'bold'))
    genderLabel.grid(row=5, column=0, padx=10, pady=10)
    genderEntry = Entry(searchStudentWindow, font=('arial', '15', 'bold'))
    genderEntry.grid(row=5, column=1, padx=10, pady=10)

    dobLabel = Label(searchStudentWindow, text="Date of Birth", font=('arial', '15', 'bold'))
    dobLabel.grid(row=6, column=0, padx=10, pady=10)
    dobEntry = Entry(searchStudentWindow, font=('arial', '15', 'bold'))
    dobEntry.grid(row=6, column=1, padx=10, pady=10)

    addStudentButton = ttk.Button(searchStudentWindow, text='Search Student', command=search)
    addStudentButton.grid(row=7, columnspan=2, padx=10, pady=10)

def delete():
    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    id=content['values'][0]
    query="delete from student where id=%s"
    myCursor.execute(query,(id))
    con.commit()
    messagebox.showinfo("Deleted",f'This {id} is deleted success')
    show()
def connect_db():
    def connect():
        global myCursor, con
        try:
            # for DEV purpose
            con = pymysql.connect(host="localhost", user="root", password="")
            # con=pymysql.connect(host=hostNameEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
            myCursor = con.cursor()
            messagebox.showinfo('success', 'Database connection is success', parent=connectWindow)
            connectWindow.destroy()
        except:
            messagebox.showerror('Error', 'Invalid input', parent=connectWindow)
            return

        try:
            query = "create database student"
            myCursor.execute(query)
            query = "use student"
            myCursor.execute(query)
            query = "CREATE TABLE `student`.`student` (`id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(255) NULL , `mobile_no` VARCHAR(30) NULL , `email` VARCHAR(150) NULL , `address` VARCHAR(255) NULL , `gender` VARCHAR(10) NULL , `dob` VARCHAR(30) NULL , `added_date` VARCHAR(30) NULL , `added_time` VARCHAR(30) NULL , PRIMARY KEY (`id`));"
            myCursor.execute(query)
        except:
            query = "use student"
            myCursor.execute(query)

        addButton.config(state=NORMAL)
        searchButton.config(state=NORMAL)
        deleteButton.config(state=NORMAL)
        updateButton.config(state=NORMAL)
        showButton.config(state=NORMAL)
        exportButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)

        show()

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+200+200')
    connectWindow.title('Database Connection')
    connectWindow.resizable(False, False)

    hostNameLabel = Label(connectWindow, text="Host Name", font=('arial', 15, 'bold'))
    hostNameLabel.grid(row=0, column=0, padx=10, pady=10)

    hostNameEntry = Entry(connectWindow, font=('arial', 15, 'bold'))
    hostNameEntry.grid(row=0, column=1, padx=10, pady=10)

    usernameLabel = Label(connectWindow, text="Username", font=('arial', 15, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=10, pady=10)

    usernameEntry = Entry(connectWindow, font=('arial', 15, 'bold'))
    usernameEntry.grid(row=1, column=1, padx=10, pady=10)

    passwordLabel = Label(connectWindow, text="Password", font=('arial', 15, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=10, pady=10)

    passwordEntry = Entry(connectWindow, font=('arial', 15, 'bold'))
    passwordEntry.grid(row=2, column=1, padx=10, pady=10)

    connectButton = ttk.Button(connectWindow, text="Connect", command=connect)
    connectButton.grid(row=3, columnspan=2, padx=10, pady=10)


count = 0
text = ""


def slider():
    global count, text
    if count == len(s):
        count = 0
        text = ""
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)


def clock():
    date = time.strftime("%d/%m/%Y")
    currentTime = time.strftime("%H:%M:%S")
    dateTimeLabel.config(text=f'    Date: {date}\nTime: {currentTime}')
    dateTimeLabel.after(1000, clock)


# GUI section
root = ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('arc')

root.geometry("1280x800+0+0")
root.title("Student Management System")
root.resizable(False, False)

dateTimeLabel = Label(root, font=("times new roman", 20, 'bold'))
dateTimeLabel.place(x=5, y=5)
clock()

s = "Student Management System"
sliderLabel = Label(root, text=s, font=("times new roman", 30, 'bold'))
sliderLabel.place(y=5, x=250)
slider()

connectButton = ttk.Button(root, text="Connect to DB", padding=10, command=connect_db)
connectButton.place(y=5, x=1000)

# LEFT
leftFrame = Frame(root)
leftFrame.place(y=100, x=25, width=300, height=650)

logoImage = PhotoImage(file="logo.png")
logoLabel = Label(leftFrame, image=logoImage)
logoLabel.grid(row=0, column=0)

addButton = ttk.Button(leftFrame, text="Add Student", padding=5, width=25, state=DISABLED, command=addStudent)
addButton.grid(row=1, column=0, pady=20)

searchButton = ttk.Button(leftFrame, text="Search Student", padding=5, width=25, state=DISABLED, command=searchStudent)
searchButton.grid(row=2, column=0, pady=20)

deleteButton = ttk.Button(leftFrame, text="Delete Student", padding=5, width=25, state=DISABLED,command=delete)
deleteButton.grid(row=3, column=0, pady=20)

updateButton = ttk.Button(leftFrame, text="Update Student", padding=5, width=25, state=DISABLED,command=update)
updateButton.grid(row=4, column=0, pady=20)

showButton = ttk.Button(leftFrame, text="Show Student", padding=5, width=25, state=DISABLED,command=show)
showButton.grid(row=5, column=0, pady=20)

exportButton = ttk.Button(leftFrame, text="Export Student", padding=5, width=25, state=DISABLED)
exportButton.grid(row=6, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text="Exit", padding=5, width=25, state=DISABLED)
exitButton.grid(row=7, column=0, pady=20)

# RIGHT
rightFrame = Frame(root)
rightFrame.place(x=350, y=100, width=850, height=650)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame,
                            columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date',
                                     'Added Time'), xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

studentTable.pack(fill=BOTH, expand=1)

studentTable.heading("Id", text="ID")
studentTable.heading("Name", text="Name")
studentTable.heading("Mobile No", text="Mobile No")
studentTable.heading("Email", text="Email")
studentTable.heading("Address", text="Address")
studentTable.heading("Gender", text="Gender")
studentTable.heading("D.O.B", text="D.O.B")
studentTable.heading("Added Date", text="Added Date")
studentTable.heading("Added Time", text="Added Time")

studentTable.config(show="headings")

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

root.mainloop()
