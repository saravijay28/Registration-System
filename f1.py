from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("online course registration")
image=Image.open("classroom.jpg")
img=image.resize((1500,650))
img1=ImageTk.PhotoImage(img)
label=Label(root,fg="black",image = img1)
#tk.Label(bg="yellow")
label.grid(row=2, column=3)
label.pack()
def continue_file():
  root.destroy()
  import main
                                   
Button_continue=Button(root,text="start",fg="white",width=150,height=1,font=("calibri",14,"bold"),bg="blue",command=continue_file)
#Button_continue=Button(root,text="cancel",fg
Button_continue.pack()
root.mainloop()