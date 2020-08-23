from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
#using tkinter 
root = Tk()
#The title of the window application
root.title("ATTENDANCE RECORDING DURING COVID-19 PANDEMIC")
#The size of the window
root.geometry("700x900")

#welcoming title and its grid
lbl = Label(root, text = "Welcome to TIES Attendance Recorder",fg="darkblue", font=("Times New Roman",20,"bold","underline"))
lbl.grid(column=0, row=0, padx=70, pady=40)

#explanation of the application in BM and its grid
lbl = Label(root, text = "Bagaimana Attendance Recorder berfungsi?",fg="indigo", font=("Times New Roman",14,"bold"))
lbl.grid(column=0, row=1,pady=5)
lbl = Label(root, text= "Dengan menggunakan aplikasi ini, anda akan membantu\n KKM untuk mengesan pelajar UniMAP yang mempunyai\n simptom-simptom COVID-19 ataupun kontak rapat\n dengan pesakit COVID-19.", fg="black",font=("Courier",12))
lbl.grid(column=0, row=2)

#explanation of the application in English and its grid
lbl = Label(root, text = "How Attendance Recorder works?",fg="indigo", font=("Times New Roman",14,"bold"))
lbl.grid(column=0, row=3,pady=5)
lbl =Label(root, text="By using this application, you will help the MOH to\n keep track of the UniMAP students that are in close\n contact with a COVID-19 patient or any suspects\n that might be influenced with COVID-19.",fg="black",font=("Courier",12))
lbl.grid(column=0,row=4)
#creating a new window using function
def createsecWindow():
    secWindow = tk.Tk()
    tabparent= ttk.Notebook(secWindow)
    tab1= ttk.Frame(tabparent)
    tab2= ttk.Frame(tabparent)
    tabparent.add(tab1, text = 'Detail Attendance')
    tabparent.add(tab2, text ='Screening Process')
    tabparent.grid()
<<<<<<< HEAD
<<<<<<< HEAD
#screening process (tab 2 )
=======
=======
>>>>>>> b0cf5f0fd8250f3f3fa49df965f39deedebb3efb
    lblName = Label(tab1, text = "Student's Name  : ").grid(column=0, row=1)
    enttemp = Entry(tab1, width = 40 ).grid (column=1, row=1, padx=50, pady=30)
    lblProgram = Label(tab1, text = "Program  : ").grid(column=0, row=2)
    enttemp = Entry(tab1, width = 40 ).grid (column=1, row=2, padx=50, pady=30)
    lblMatric = Label(tab1, text = "Matric No.  : ").grid(column=0, row=3)
    enttemp = Entry(tab1, width = 40 ).grid (column=1, row=3, padx=50, pady=30)
    lblPhone = Label(tab1, text = "Phone No.  : ").grid(column=0, row=4)
    enttemp = Entry(tab1, width = 40 ).grid (column=1, row=4, padx=50, pady=30)
<<<<<<< HEAD
=======

>>>>>>> b0cf5f0fd8250f3f3fa49df965f39deedebb3efb


>>>>>>> b0cf5f0fd8250f3f3fa49df965f39deedebb3efb
    lbl_name = Label(tab2, text = "Your Body Temprature :")
    lbl_name.grid(column=0, row=1)
    enttemp = Entry(tab2, width = 40 ) .grid (column=1, row=1, padx=50, pady=50)
    lbl.name = Label(tab2, text = "symptoms of infection : ").grid (column=0, row=2,)
    CheckVar1 = IntVar ()
    CheckVar2 = IntVar ()
    CheckVar3 = IntVar ()
    CheckVar4 = IntVar ()
    CheckVar5 = IntVar ()
    CheckVar6 = IntVar ()
    CheckVar7 = IntVar ()
    Checksymptoms1 = Checkbutton (tab2, text="Fever", variable = CheckVar1,onvalue = 1, offvalue = 0,width = 20).grid (column =1,row=3,padx=50) 
    Checksymptoms2 = Checkbutton (tab2, text="Dry Cough", variable = CheckVar2,onvalue = 1, offvalue = 0,width = 20).grid (column =1,row=4,padx=50) 
    Checksymptoms3 = Checkbutton (tab2, text="Sore Throat", variable = CheckVar3,onvalue = 1, offvalue = 0,width = 20).grid (column =1,row=5,padx=50)
    Checksymptoms4 = Checkbutton (tab2, text="Tiredness", variable = CheckVar4,onvalue = 1, offvalue = 0,width = 20).grid (column =1,row=6,padx=50)
    Checksymptoms5 = Checkbutton (tab2, text="Nasal Congestion", variable = CheckVar5,onvalue = 1, offvalue = 0,width = 20).grid (column =1,row=7,padx=50)
    Checksymptoms6 = Checkbutton (tab2, text="Runny Nose", variable = CheckVar6,onvalue = 1, offvalue = 0,width = 20).grid (column =1,row=8,padx=50)
    Checksymptoms7 = Checkbutton (tab2, text="Aches and Pains", variable = CheckVar7,onvalue = 1, offvalue = 0,width = 20).grid (column =1,row=9,padx=50)
    btn = Button(tab2,text='SUBMIT')
    btn.grid(column=1,row=11, padx=50)
    tab2.mainloop()
#button to next page and its grid
btn = Button(root, text="Let's Get Started",bg="black",fg="white",font=("starline",14),command=createsecWindow)
btn.grid(column=0,row=5)

img= ImageTk.PhotoImage(Image.open("covid.png"))
imgDisplay=Label(root, image=img)
imgDisplay.grid(column=0, row=6)
img1= ImageTk.PhotoImage(Image.open("image.jpg"))
imgDisplay=Label(root, image=img1)
imgDisplay.grid(column=0, row=7)


#This will loop the application until the user ends it
root.mainloop()