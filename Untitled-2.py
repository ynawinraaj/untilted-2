from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTK

# Setting up Main Window
root=Tk()
root.title("denomination counter")
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload=Image.open("app_img.jpg")

# Resize the image using resize() method
upload=upload.resize((300,300))
image=ImageTK.PhotoImage(upload)
label=Label(root,image=image,bg='light blue')
label.place(x=180,y=20)

label1=Label(root,text="hey user welcome to denomination counter app")
label.place(relx=0.5,y=340,anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox=messagebox.showinfo("alert","do you want to calculate denomination count?")
    if MsgBox=='ok':
        topwin()
        
# Adding Buttons to the main window
button1=Button(root,text="lets get started",command=msg,bg='brown',fg='white')
button1.place(x=260,y=360)

# Function for opening new/top window
def topwin():
    top=Toplevel()
    top.title("denomination calculation")
    top.configure(bg='light gery')
    top.geometry("600x350+50+50")
    label=Label(top,text="enter the total amount",bg='light grey')
    entry=Entry(top)
    lbl=Label(top,text="here are the number of the notes for each denominatin",bg='light grey')
    l1=Label(top,text="2000",bg='light grey')
    l2=Label(top,text="500",bg='light grey')
    l3=Label(top,text="200",bg='light grey')
    
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

# Centering Widgets in the Top Window
label.place(x=230, y=50   )
entry.place(x=200, y=80   )
btn.place(x=240, y=120   )
lbl.place(x=140, y=170   )

l1.place(x=180, y=200   )
l2.place(x=180, y=230   )
l3.place(x=180, y=260   )

t1.place(x=270, y=200)
t2.place(x=270, y=230)
t3.place(x=270, y=260)

top.mainloop()

root.mainloop()
