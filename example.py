#print(" hai from pc 1 ")
#print(" hi from shaheera ")

from tkinter import*
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
    secWindow= tk.Toplevel(root)
    lbl=Label(secWindow,text="Name")
    lbl.grid(column=0,row=0)

#button to next page and its grid
btn = Button(root, text="Let's Get Started",bg="black",fg="white",font=("starline",14),command=createsecWindow)
btn.grid(column=0,row=5)

covid_photo = PhotoImage(file="C:\\Users\\user\\Documents\\python codes\\mini project\\image.png")
lbl=Label(root, image=covid_photo)
lbl.grid(column=0, row=6)


#This will loop the application until the user ends it
root.mainloop()