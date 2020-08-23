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
    lblName = Label(group1, text = "Name :")
    lblAddress = Label(group1, text = "Address :")
    lblPhone = Label(group1, text = "Phone :")
    lblEmail = Label(group1, text = "Email :")
    tabparent.add(tab2, text ='Screening process')
    lbl_name = Label(tab2, text = "Your Body Temprature :")
    lbl_name.grid(column=0, row=1, padx=50, pady=50)
    #enttemp = Entry(tab2, width = 40 ) .grid (column=1, row=1, padx=50, pady=50)
    #lbl.name = Label(tab2, text = "symptoms of infection : ") .grid (column=2, row=2)
    
    #Checkvar1 = Intvar ()
    #Checkvar2 = Intvar ()
    #Checkvar3 = Intvar ()
    #Checkvar4 = Intvar ()
    #Checkvar5 = Intvar ()
    #Checkvar6 = Intvar ()
    #Checkvar7 = Intvar ()
    #Checksymptoms1 = Checkbutton (tab2, text "Fever", variables = Checkvar1) .grid (column = 0)
    #tabparent.grid()
    
   


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