from tkinter import *
import sqlite3
from tkinter import messagebox
import re


def clear():
    # clear output area
    #   output.delete(0.0,END)

    entry_name.delete(0, END)
    entry_password.delete(0, END)
    entry_contact.delete(0, END)
    entry_email.delete(0, END)
    entry_age.delete(0, END)
    # clear checkbox and radio
    #checkbox1.set(0)
    #checkbox2.set(0)
    #checkbox3.set(0)
    gender.set(0)


# Callback functions

def checkname(name):
    if name.isalnum():
        return True
    if name == "":
        return True
    else:
        messagebox.showwarning("Invalid", "Not allowed " + name[-1])
        return False


"""
^                                            Match the beginning of the string
(?=.*[0-9])                                  Require that at least one digit appear anywhere in the string
(?=.*[a-z])                                  Require that at least one lowercase letter appear anywhere in the string
(?=.*[A-Z])                                  Require that at least one uppercase letter appear anywhere in the string
(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\])    Require that at least one special character appear anywhere in the string
.{8,32}                                      The password must be at least 8 characters long, but no more than 32
$                                            Match the end of the string.
"""


def checkpassword(password):
    if len(password) <= 20:
        if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))", password):
            return True

        messagebox.showwarning("Invalid", "Enter valid password")
        return False
    else:
        messagebox.showwarning("Invalid", "Length try to exceed")
        return False


def checkcontact(con):
    if con.isdigit():
        return True
    if len(str(con)) == 0:
        return True


    else:
        messagebox.showwarning("Invalid", "Invalid Entry")
        return False


def checkemail(email):
    if len(email) > 7:
        if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email):
            return True


        else:
            messagebox.showwarning("Alert", "Invalid E-mail enter by user")
            return False
    else:
        messagebox.showwarning("Alert", "Email length is too small")


# validate all field at submit time
def shifting_form_2():
    win.destroy()
    import success
def validations():
    x = y = 0
    if name.get() == "":
        messagebox.showinfo("Alert", "Enter your name first")
    elif password.get() == "":
        messagebox.showinfo("Alert", "Enter Password")
    elif contact.get() == "" or len(contact.get()) != 10:
        messagebox.showinfo("Alert", "Enter valid Contact ")
    elif email.get() == "":
        messagebox.showinfo("Alert", "Enter Email")
    elif age.get() == "":
        messagebox.showinfo("Alert", "Enter Age")
    elif gender.get() == 0:
        messagebox.showinfo("Alert", "Select Gender")
    elif country.get() == "" or country.get() == "Select your country":
        messagebox.showinfo("Alert", "Select country")
    elif checkbox1.get() == 0 and checkbox2.get() == 0 and checkbox3.get() == 0:
        messagebox.showinfo("Alert", "Select language")
    elif email.get() != None and password.get() != None:

        x = checkemail(email.get())
        y = checkpassword(password.get())
        print(x, y)
    if (x == True) and (y == True):
        prog = []
        name1 = name.get()
        pas1 = password.get()
        cont1 = contact.get()
        email1 = email.get()
        age1 = age.get()
        gvar = gender.get()
        cnt = country.get()
        #course = checkbox1.get(), checkbox2.get(), checkbox3.get()
        course = str(course)
        shifting_form_2()
        # print(name1,pas1,cont1,email1,age1,gvar,cnt,prog,type(name1),type(pas1),type(cont1),type(email1),type(age1),type(gvar),type(cnt),type(prog))
        # connection with db
        conn = sqlite3.connect('Register1.db')
        with conn:
            cursor = conn.cursor()
            # querries
            cursor.execute('CREATE TABLE IF NOT EXISTS  Registration(Name TEXT,Password TEXT,Contact Text,Email TEXT,Age Text,\
                                  Gender Number,Country Text,Prog Text)')
            cursor.execute(
                'INSERT INTO Registration(Name,Password,Contact,Email,Age,Gender,Country,Prog) VALUES(?,?,?,?,?,?,?,?)',
                (name1, pas1, cont1, email1, age1, gvar, cnt, prog))

        conn.commit()


def view():
    lx = [name.get(), "\n", password.get(), "\n", contact.get(), "\n", email.get(), "\n",
          age.get(), "\n", gender.get(), "\n", country.get(), "\n", course.get()]
    messagebox.showinfo("Details", lx)


# GUI

win = Tk()
win.geometry("500x600")
win.minsize(width=1500,height=800)
win.title("Course Registration Form")
win["bg"] = "sky blue"

# creating data selection variable on gui
name = StringVar()
password = StringVar()
contact = StringVar()
email = StringVar()
age = StringVar()
gender = IntVar()
country = StringVar()
course = StringVar()
#checkbox1 = IntVar()

#checkbox2 = IntVar()
#checkbox3 = IntVar()

# Form Title
label_title = Label(win, text="Course Registration Form", width=30, font=("bold", 30)).place(x=270, y=53)

# Create fields
label_name = Label(win, text="Your Name", width=30,font=(30)).place(x=300, y=160)
entry_name = Entry(win, width=25,font=(30), textvariable=name)
entry_name.place(x=700, y=160)
validate_name = win.register(checkname)  # validation register
entry_name.config(validate="key", validatecommand=(validate_name, "%P"))  # validation configure

label_password = Label(win, text="Password", width=30,font=(30)).place(x=300, y=210)
entry_password = Entry(win, textvariable=password, width=25,font=(30))
entry_password.place(x=700, y=210)

label_contact = Label(win, text="Contact", width=30,font=(30)).place(x=300, y=260)
entry_contact = Entry(win, textvariable=contact, width=25,font=(30))
entry_contact.place(x=700, y=260)
validate_contact = win.register(checkcontact)  # validation register
entry_contact.config(validate="key", validatecommand=(validate_contact, "%P"))

label_email = Label(win, text="Email Id", width=30,font=(30)).place(x=300, y=310)
entry_email = Entry(win, textvariable=email, width=25,font=(30))
entry_email.place(x=700, y=310)

label_age = Label(win, text="Your Age", width=30,font=(30)).place(x=300, y=360)
entry_age = Spinbox(win, textvariable=age, width=24,from_=0, to_=150,font=(28))
entry_age.place(x=700, y=360)

label_gender = Label(win, text="Gender", width=30,font=(36)).place(x=300, y=410)
g_radio_male = Radiobutton(win, text="Male", padx=5, variable=gender, value=1,width=7,font=(16)).place(x=700, y=410)
g_radio_female = Radiobutton(win, text="Female", padx=20, variable=gender,width=7 ,value=2,font=(16)).place(x=800,y=410)

label_country = Label(win, text="Your Country", width=30,font=(30)).place(x=300, y=460)
list1 = ['Canada', 'India', 'UK', 'Nepal', 'Iceland', 'South Africa'];
droplist = OptionMenu(win, country, *list1)
droplist.config(width=21,font=(7))
country.set('Select your country')
droplist.place(x=700, y=460)

label_prog = Label(win, text="course", width=30,font=(30)).place(x=300, y=510)
list1 = ['Full stack', 'cybersecurity', 'AI', 'Bigdata', 'Blockchain', 'cloud computing'];
droplist = OptionMenu(win, course, *list1)
droplist.config(width=21,font=(7))
course.set('Select your course')
droplist.place(x=700, y=510)
#entry_check1 = Checkbutton(win, text="java", variable=checkbox1,font=(25)).place(x=700, y=460)
#entry_check2 = Checkbutton(win, text="Python", variable=checkbox2,font=(25)).place(x=750, y=460)
#entry_check3 = Checkbutton(win, text="C", variable=checkbox3,font=(25)).place(x=800, y=460)

Button(win, text='submit', width=15,font=(18),bg='blue', fg='white', command=shifting_form_2).place(x=550, y=600)
Button(win, text='clear data', width=15,font=(18),bg='blue', fg='white', command=clear).place(x=330, y=600)
Button(win, text='Check', width=15,font=(18),bg='blue', fg='white', command=view).place(x=780, y=600)

win.mainloop()



