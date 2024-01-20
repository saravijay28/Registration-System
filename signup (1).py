#---Import Librarires
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#----Functions/Actions

def validation():
    if name.get()!="" and email.get()!="" and password.get()!="" and gender.get()!="" and age.get()!="":
        email_check=email_validation()
        password_check=password_validataion()
        duplicate_check=duplicates()
        if email_check:
            if duplicate_check:
                messagebox.showinfo("information","User Email Already Exist")
            elif password_check:
                insertion_data()
                messagebox.showinfo("information","Data Inserted Sucessfully")
                shifting_form()
            else:
                messagebox.showerror("Error","Password should be (max 7 characters ,upper and lower case letter , number and symbol)")
        else:
            messagebox.showerror("Error","Email Fromat Is Not invalid")
    else:
        messagebox.showerror("Error","Fill All The Required Feilds")

def shifting_form():
    screen.destroy()
    import login

def insertion_data():
    with open("insertion.txt",'+a') as wr:
        wr.write(f"{name.get()},{email.get()},{password.get()},{gender.get()},{age.get()}\n")
def email_validation():
    temp = email.get() 
    count=-1
    for i in temp:
        count+=1
        if i=="@":
            if temp[count:len(temp)]=="@gmail.com":
                return True
            else:
                return False
    else:
        return False

def password_validataion():
    temp = password.get()
    if len(temp)>=8:
        a,b,c,d=False,False,False,False        
        #use multi varaible for checking pass_validatiom
        for i in temp:
            x = ord(i)
            if x>=65 and x<=90:
                a=True
            elif x>=97 and x<=122:
                b=True
            elif x>=48 and x<=57:
                c=True
            else:
                d=True
        if a and b and c and d:
            return True
        else:
            return False
    else:
        return False
def duplicates():
    with open("insertion.txt") as rd:
        data = rd.readline()
        while data!="":
            collection = data.split(",")
            if collection[1]==email.get():
                return True
            data = rd.readline()
        else:
            return False

#---Graphical Interface
screen = Tk()
#---variables
name = StringVar()
email = StringVar()
password = StringVar()
gender = StringVar()
age = StringVar()
    #screen-ui
screen.geometry("700x600")
screen.maxsize(width="1000",height="900")
screen.minsize(width="900",height="800")
screen.config(bg="violet")
screen.title("Registration")
    #Signuop Title
title = Label(text="SIGN UP",font=("Arial",35,"bold"),padx="5",pady="5",bg="violet",fg="WHITE").pack(pady="50")
    #signup frame
signup_frame = Frame(screen,width="650",height="700",bg="white")
signup_frame.place(x="240",y="200")
    # signup frame widgets

#widget 1
fullname_label = Label(signup_frame,width="15",padx="5",pady="5",text="User Name",bg="white",fg="black",font=("Calibri",15,'bold')).grid(row=0,column=0,padx="5",pady="5")
fullname_entry = Entry(signup_frame,textvariable=name,selectbackground="deep sky blue",selectforeground="deep sky blue",font=("Calibri",15,"italic")).grid(row=0,column=1,padx="15",pady="5")
#widget 2
email_label = Label(signup_frame,width="15",padx="5",pady="5",text="User Email",bg="white",fg="black",font=("Calibri",15,'bold')).grid(row=1,column=0,padx="5",pady="5")
email_entry = Entry(signup_frame,textvariable=email,selectbackground="deep sky blue",selectforeground="black",font=("Calibri",15,"italic")).grid(row=1,column=1,padx="15",pady="5")
#widget 3
password_label = Label(signup_frame,width="15",padx="5",pady="5",text="User Password",bg="white",fg="black",font=("Calibri",15,'bold')).grid(row=2,column=0,padx="5",pady="5")
password_entry = Entry(signup_frame,show="*",textvariable=password,selectbackground="deep sky blue",selectforeground="black",font=("Calibri",15,"italic")).grid(row=2,column=1,padx="15",pady="5")
#widget 4
#phone_label = Label(signup_frame,width="15",padx="5",pady="5",text="User Email",bg="yellow2",fg="deep sky blue",font=("Calibri",15,'bold')).grid(row=3,column=0,padx="5",pady="5")
#phone_entry = Entry(signup_frame,textvariable=phone,selectbackground="deep sky blue",selectforeground="black",font=("Calibri",15,"italic")).grid(row=3,column=1,padx="15",pady="5")
#widget 5
#gender.set("Radio")
#gender_label = Label(signup_frame,width="15",padx="5",pady="5",text="User Gender",bg="white",fg="deep sky blue",font=("Calibri",15,'bold')).grid(row=4,column=0,padx="5",pady="5")
#gander_male = Radiobutton(signup_frame,text="Male",bg="white",value="Male",width="5",variable=gender).place(x="190",y="155")
#gander_female = Radiobutton(signup_frame,text="Female",bg="white",width="5",value="Female",variable=gender).place(x="260",y="155")
#gander_others = Radiobutton(signup_frame,text="Others",bg="white",width="5",value="Others",variable=gender).place(x="328",y="155")
#widget 5
#widget 5
#age_label = Label(signup_frame,width="15",padx="5",pady="5",text="User Age",bg="white",fg="deep sky blue",font=("Calibri",15,'bold')).grid(row=4,column=0,padx="5",pady="5")
#values = [int(i) for i in range(9,111)]
#age.set("")
#age_combo = ttk.Combobox(signup_frame,value=values,width="25",state="readonly",textvariable=age,font=("Arial",10,"italic")).grid(row=4,column=1)
#widget 6

signup_btn = Button(signup_frame,text="Sign Up",width="30",bg="deep sky blue",fg="white",font=("Arial",15,"italic"),command=validation).grid(row=5,columnspan=2,pady="15",padx="10")



screen.mainloop()