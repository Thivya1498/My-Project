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

#screening process (tab 2 )

    lblName = Label(tab1, text = "Student's Name  : ").grid(column=0, row=1)
    enttemp = Entry(tab1, width = 40 ).grid (column=1, row=1, padx=50, pady=30)
    lblProgram = Label(tab1, text = "Program  : ").grid(column=0, row=2)
    enttemp = Entry(tab1, width = 40 ).grid (column=1, row=2, padx=50, pady=30)
    lblMatric = Label(tab1, text = "Matric No.  : ").grid(column=0, row=3)
    enttemp = Entry(tab1, width = 40 ).grid (column=1, row=3, padx=50, pady=30)
    lblPhone = Label(tab1, text = "Phone No.  : ").grid(column=0, row=4)
    enttemp = Entry(tab1, width = 40 ).grid (column=1, row=4, padx=50, pady=30)


    lbl_name = Label(tab2, text = "Your Body Temprature :")
    lbl_name.grid(column=0, row=1)
    enttemp = Entry(tab2, width = 40 ) .grid (column=1, row=1, padx=50, pady=50)
    lbl.name = Label(tab2, text = "symptoms of infection : ").grid (column=0, row=2,)
  
    Checksymptoms1 = Checkbutton (tab2, text="Fever/Demam", takefocus = 0).place(x = 150, y = 120)  
    Checksymptoms2 = Checkbutton (tab2, text="Dry Cough/atuk Kering",takefocus = 0).place(x = 150, y =140)   
    Checksymptoms3 = Checkbutton (tab2, text="Sore Throat/Sakit Tekak",takefocus = 0).place(x = 150, y = 160)  
    Checksymptoms4 = Checkbutton (tab2, text="Tiredness/Penat", takefocus = 0).place(x = 150, y = 180) 
    Checksymptoms5 = Checkbutton (tab2, text="Nasal Congestion/Hidung Tersumbat", takefocus = 0).place(x = 150, y = 200) 
    Checksymptoms6 = Checkbutton (tab2, text="Runny Nose/Hidung Berair",takefocus = 0).place(x = 150, y = 220) 
    Checksymptoms7 = Checkbutton (tab2, text="Aches and Pains/sakit-sakit badan",takefocus = 0).place(x=150 ,  y = 240) 
    btn = Button(tab2,text='SUBMIT')
    btn.grid(column=1,row=6, padx=170)
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