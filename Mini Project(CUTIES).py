""" 
GOOD JOB :)
"""

from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter as tk
import sqlite3
import tkinter.messagebox

#using tkinter 
root = Tk()
#The title of the window application
root.title("ATTENDANCE RECORDING DURING COVID-19 PANDEMIC")
#The size of the window
root.geometry("700x900")
#the background colour of the window
root['bg']="IndianRed3"

#welcoming title and its grid
lbl = Label(root, text = "Welcome to CUTIES Attendance Recorder",bg="yellow3",fg="darkblue", font=("Times New Roman",20,"bold","underline"))
lbl.grid(column=0, row=0, padx=70, pady=40)

#explanation of the application in BM and its grid
lbl = Label(root, text = "Bagaimana Attendance Recorder berfungsi?",bg="salmon",fg="indigo", font=("Times New Roman",14,"bold"))
lbl.grid(column=0, row=1,pady=5)
lbl = Label(root, text= "Dengan menggunakan aplikasi ini, anda akan membantu\n KKM untuk mengesan pelajar UniMAP yang mempunyai\n simptom-simptom COVID-19 ataupun kontak rapat\n dengan pesakit COVID-19.",bg="yellowgreen", fg="black",font=("Courier",12))
lbl.grid(column=0, row=2)

#explanation of the application in English and its grid
lbl = Label(root, text = "How Attendance Recorder works?",bg="salmon",fg="indigo", font=("Times New Roman",14,"bold"))
lbl.grid(column=0, row=3,pady=5)
lbl =Label(root, text="By using this application, you will help the MOH to\n keep track of the UniMAP students that are in close\n contact with a COVID-19 patient or any suspects\n that might be influenced with COVID-19.",bg="yellowgreen",fg="black",font=("Courier",12))
lbl.grid(column=0,row=4)

#creating a new window using function
def createsecWindow():
    secWindow = tk.Tk()
    #title of the new window
    secWindow.title("Personal Information")
    #creating tab widget
    tabparent= ttk.Notebook(secWindow)
    tab1= ttk.Frame(tabparent)#first tab
    tab2= ttk.Frame(tabparent)#second tab
    tab3= ttk.Frame(tabparent)#third tab

    #title of the tabs and grid
    tabparent.add(tab1, text = 'Detail Attendance')
    tabparent.add(tab2, text ='Screening Process')
    tabparent.add(tab3, text="Database")
    tabparent.grid()

    #creating a function to save the information in database
    def saveForm():
        print(entName.get())
    
    
        #Create database/connect to database
        conn = sqlite3.connect('attendance-book-data.db')

        #Create a cursor
        c = conn.cursor()
    
        c.execute("INSERT INTO Attendance(Name,Program,Matric,Phone,BodyTemperature,Symptoms) VALUES(?,?,?,?,?,?)",
              (entName.get(),entProgram.get(),entMatric.get(),entPhone.get(),entTemp.get(),entList.get(),))

        #Commit changes
        conn.commit()

        #Close Connection
        conn.close()
        
        #show message box for successful query
        tkinter.messagebox.showinfo("Success", "Data inserted successfully.")
        
        #clear the form after button is hit & show existing data
        clearEntry()
        clearTab2()
        showExisting()
        
    #creating a function to show the existing data from database
    def showExisting():
        conn = sqlite3.connect('attendance-book-data.db')  
        c = conn.cursor()
    
        #query existing record from contact table
        c.execute("SELECT * FROM Attendance")
        conn.commit()
    
        #fetch the data
        records = c.fetchall()
    
        #display the data
        rownum = 10 #to hold current row in grid, to be increased with each data existed

        for x in records:
            print(x)
            
            lblExId2 = Label(lfExistingAttendance, text=str(x[0]),bg="indian red")
            lblExId2.grid(row=rownum,column=0,padx=2,sticky=W)
            lblExName2 = Label(lfExistingAttendance, text=str(x[1]),bg="indian red")
            lblExName2.grid(row=rownum,column=1,padx=2,sticky=W)
            lblExProgram2 = Label(lfExistingAttendance, text=str(x[2]),bg="indian red")
            lblExProgram2.grid(row=rownum,column=2,padx=2,sticky=W)
            lblExMatric2 = Label(lfExistingAttendance, text=str(x[3]), bg="indian red")
            lblExMatric2.grid(row=rownum,column=3,padx=2,sticky=W)
            lblExPhone2 = Label(lfExistingAttendance, text=str(x[4]), bg="indian red")
            lblExPhone2.grid(row=rownum,column=4,padx=2,sticky=W)
            lblExTemp2 = Label(lfExistingAttendance, text=str(x[5]), bg="indian red")
            lblExTemp2.grid(row=rownum,column=5,padx=2,sticky=W)
            lblExSymptoms2 = Label(lfExistingAttendance, text=str(x[6]), bg="indian red")
            lblExSymptoms2.grid(row=rownum,column=6,padx=2,sticky=W)
            
            rownum += 1
     
        conn.close()

    #create a function to clear all the entries in tab1
    def clearEntry():
        entName.delete(0,END)
        entProgram.delete(0,END)
        entMatric.delete(0,END)
        entPhone.delete(0,END)
    
    #create a function to clear all the entries in tab2
    def clearTab2():
        entTemp.delete(0,END)
        
#showing warning sign if have high risks.
    def risk():
        
        Temp1=float(entTemp.get())
        Symptoms=(entList.get())
        #using if else according to the temperature reading
        if Temp1<=37.5 and Symptoms=="None":
            tkinter.messagebox.showinfo("Information", "Low Risk. Your Temperature is Normal. You can enter the Classroom.") 
        else:
            tkinter.messagebox.showwarning("Information", "High Risk. Your Temperature is Upnormal. You cannot enter the Classroom.")
             
#student details (tab 1)
    lblName = Label(tab1, text = "Student's Name  : ")
    lblName.grid(column=0, row=1)

    entName = Entry(tab1, width = 40,bg="indian red" )
    entName.grid (column=1, row=1, padx=50, pady=30)

    lblProgram = Label(tab1, text = "Program  : ")
    lblProgram.grid(column=0, row=2)

    entProgram = Entry(tab1, width = 40 ,bg="indian red")
    entProgram.grid (column=1, row=2, padx=50, pady=30)

    lblMatric = Label(tab1, text = "Matric No.  : ")
    lblMatric.grid(column=0, row=3)

    entMatric = Entry(tab1, width = 40,bg="indian red" )
    entMatric.grid (column=1, row=3, padx=50, pady=30)

    lblPhone = Label(tab1, text = "Phone No.  : ")
    lblPhone.grid(column=0, row=4)

    entPhone = Entry(tab1, width = 40, bg="indian red")
    entPhone.grid (column=1, row=4, padx=50, pady=30)

    lblNext =Label(tab1,text="*Please proceed to Screening to Process",fg="red")
    lblNext.grid(column=1,row=5)
    btnClear1 = Button(tab1, text="Clear",bg="coral1",font=("starline",10),command=clearEntry)
    btnClear1.grid(column=1,row=6, pady=30)

#screening process (tab 2 )
    lblTemp = Label(tab2, text = "Body Temprature :")
    lblTemp.grid(column=0, row=1)

    entTemp = Entry(tab2, width = 40 ,bg="indian red") 
    entTemp.grid (column=1, row=1, padx=50, pady=50)

    lblSymptom = Label(tab2, text = "Symptoms of Infection : ")
    lblSymptom.grid (column=0, row=2,)
   
   #using .place for accurate setting
    Checksymptoms1 = Checkbutton (tab2, text="Fever/Demam", takefocus = 0,bg="coral1").place(x = 150, y = 120)  
    Checksymptoms2 = Checkbutton (tab2, text="Dry Cough/Batuk Kering",takefocus = 0,bg="coral1").place(x = 150, y =140)   
    Checksymptoms3 = Checkbutton (tab2, text="Sore Throat/Sakit Tekak",takefocus = 0,bg="coral2").place(x = 150, y = 160)  
    Checksymptoms4 = Checkbutton (tab2, text="Tiredness/Penat", takefocus = 0,bg="coral2").place(x = 150, y = 180) 
    Checksymptoms5 = Checkbutton (tab2, text="Nasal Congestion/Hidung Tersumbat", takefocus = 0,bg="coral2").place(x = 150, y = 200) 
    Checksymptoms6 = Checkbutton (tab2, text="Runny Nose/Hidung Berair",takefocus = 0,bg="coral3").place(x = 150, y = 220) 
    Checksymptoms7 = Checkbutton (tab2, text="Aches and Pains/sakit-sakit badan",takefocus = 0,bg="coral3").place(x=150 ,  y = 240) 
    lbllist = Label(tab2, text="*Please list the symptoms below.\nIf there is none then enter 'None'. Thank You.",fg="red")
    lbllist.place(x=100,y=280)
    entList= Entry(tab2, width=60)
    entList.place(x=60,y=320)
    btnSave = Button(tab2,text='Save',bg="coral1",font=("starline",10),command=saveForm)
    btnSave.place(x= 150, y=340)
    btnSubmit = Button(tab2,text='Submit',bg="coral1",font=("starline",10),command=risk)
    btnSubmit.place(x=190, y=340)
    btnClear= Button(tab2,text="Clear",bg="coral1",font=("starline",10),command=clearTab2)
    btnClear.place(x=240,y=340)

#database(tab3)

    btnShowAll = Button(tab3, text="Show All",bg="coral1",font=("starline",10), command=showExisting)
    btnShowAll.grid(column=1,row=0)

    #creating label frame for existing attendance
    lfExistingAttendance = LabelFrame(tab3, text="My Existing Attendance", bg='indian red', width=400, height=500)
    lfExistingAttendance.grid(row=1, column=1)

    lblExId = Label(lfExistingAttendance, text="Id",bg="indian red")
    lblExId.grid(row=2,column=0,padx=2,sticky=W)
    lblExName = Label(lfExistingAttendance, text="Name",bg="indian red")
    lblExName.grid(row=2,column=1,padx=2,sticky=W)
    lblExProgram = Label(lfExistingAttendance, text="Program",bg="indian red")
    lblExProgram.grid(row=2,column=2,padx=2,sticky=W)
    lblExMatric = Label(lfExistingAttendance, text="Matric",bg="indian red")
    lblExMatric.grid(row=2,column=3,padx=2,sticky=W)
    lblExPhone = Label(lfExistingAttendance, text="Phone",bg="indian red")
    lblExPhone.grid(row=2,column=4,padx=2,sticky=W)
    lblExTemp= Label(lfExistingAttendance, text="Body Temperature",bg="indian red")
    lblExTemp.grid(row=2,column=5,padx=2,sticky=W)
    lblExSymptoms= Label(lfExistingAttendance, text="Symptoms",bg="indian red")
    lblExSymptoms.grid(row=2,column=6,padx=2,sticky=W)

    lblThank= Label(tab3, text="Thank you for using CUTIES Attendance Recorder.\n Stay Safe, Stay Healthy and Please wear Mask",bg="coral1",fg="darkblue", font=("Times New Roman",15,"underline"))
    lblThank.grid(column=1, row=12,padx=20)

#button to next page and its grid
btn = Button(root, text="Let's Get Started",bg="black",fg="white",font=("starline",14),command=createsecWindow)
btn.grid(column=0,row=5)

#creating image in the first window.
img= ImageTk.PhotoImage(Image.open("covid.png"))
imgDisplay=Label(root, image=img,bg="IndianRed3")
imgDisplay.grid(column=0, row=6)
img1= ImageTk.PhotoImage(Image.open("image.jpg"))
imgDisplay=Label(root, image=img1,bg="IndianRed3")
imgDisplay.grid(column=0, row=7)

#This will loop the application until the user ends it
root.mainloop()