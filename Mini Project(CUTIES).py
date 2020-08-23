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
    tabparent= ttk.Notebook(secWindow)
    tab1= ttk.Frame(tabparent)
    tab2= ttk.Frame(tabparent)
    tab3= ttk.Frame(tabparent)
    tabparent.add(tab1, text = 'Detail Attendance')
    tabparent.add(tab2, text ='Screening Process')
    tabparent.add(tab3, text="Database")
    tabparent.grid()

    def submitForm():
        print(entName.get())
    
    
        #Create database/connect to database
        conn = sqlite3.connect('attendance-book-data.db')

        #Create a cursor
        c = conn.cursor()
    
        c.execute("INSERT INTO Attendance(Name,Program,Matric,Phone,BodyTemperature) VALUES(?,?,?,?,?)",
              (entName.get(),entProgram.get(),entMatric.get(),entPhone.get(),entTemp.get(),))

        #Commit changes
        conn.commit()

        #Close Connection
        conn.close()
        
        #show message box for successful query
        tkinter.messagebox.showinfo("Success", "Data inserted successfully.")
        
        #clear the form after button is hit & show existing data
        clearEntry()
        showExisting()
        
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
            
            lblExId2 = Label(lfExistingAttendance, text=str(x[0]), bg="white")
            lblExId2.grid(row=rownum,column=0,padx=2,sticky=W)
            lblExName2 = Label(lfExistingAttendance, text=str(x[1]), bg="white")
            lblExName2.grid(row=rownum,column=1,padx=2,sticky=W)
            lblExProgram2 = Label(lfExistingAttendance, text=str(x[2]), bg="white")
            lblExProgram2.grid(row=rownum,column=2,padx=2,sticky=W)
            lblExMatric2 = Label(lfExistingAttendance, text=str(x[3]), bg="white")
            lblExMatric2.grid(row=rownum,column=3,padx=2,sticky=W)
            lblExPhone2 = Label(lfExistingAttendance, text=str(x[4]), bg="white")
            lblExPhone2.grid(row=rownum,column=4,padx=2,sticky=W)
            lblExTemp2 = Label(lfExistingAttendance, text=str(x[5]), bg="white")
            lblExTemp2.grid(row=rownum,column=5,padx=2,sticky=W)
            
            rownum += 1
     
        conn.close()

    def clearEntry():
        entName.delete(0,END)
        entProgram.delete(0,END)
        entMatric.delete(0,END)
        entPhone.delete(0,END)
    def clearTab2():
        entTemp.delete(0,END)
        

    #Warning if have risk or not.
    def risk():
        x=Tk()
        if entTemp <=37:
            messagebox.showinfo("Information", "Your Temperature is Normal.") 
        elif enttemp <=38:
            messagebox.showinfo("Information", "Attention is need to be given to your Temperature and You can't get in to the Classroom")
        else:
            messagebox.showinfo("Information", "Medicine from docter is needed")
            
        x.mainloop()  
#student details (tab 1)
    lblName = Label(tab1, text = "Student's Name  : ")
    lblName.grid(column=0, row=1)

    entName = Entry(tab1, width = 40 )
    entName.grid (column=1, row=1, padx=50, pady=30)

    lblProgram = Label(tab1, text = "Program  : ")
    lblProgram.grid(column=0, row=2)

    entProgram = Entry(tab1, width = 40 )
    entProgram.grid (column=1, row=2, padx=50, pady=30)

    lblMatric = Label(tab1, text = "Matric No.  : ")
    lblMatric.grid(column=0, row=3)

    entMatric = Entry(tab1, width = 40 )
    entMatric.grid (column=1, row=3, padx=50, pady=30)

    lblPhone = Label(tab1, text = "Phone No.  : ")
    lblPhone.grid(column=0, row=4)

    entPhone = Entry(tab1, width = 40 )
    entPhone.grid (column=1, row=4, padx=50, pady=30)

    btnClear1 = Button(tab1, text="Clear",command=clearEntry)
    btnClear1.grid(column=1,row=5, pady=30)

#screening process (tab 2 )
    lblTemp = Label(tab2, text = "Body Temprature :")
    lblTemp.grid(column=0, row=1)

    entTemp = (Entry(tab2, width = 40 ) )
    entTemp.grid (column=1, row=1, padx=50, pady=50)

    lblSymptom = Label(tab2, text = "Symptoms of Infection : ")
    lblSymptom.grid (column=0, row=2,)
   
    Checksymptoms1 = Checkbutton (tab2, text="Fever/Demam", takefocus = 0).place(x = 150, y = 120)  
    Checksymptoms2 = Checkbutton (tab2, text="Dry Cough/Batuk Kering",takefocus = 0).place(x = 150, y =140)   
    Checksymptoms3 = Checkbutton (tab2, text="Sore Throat/Sakit Tekak",takefocus = 0).place(x = 150, y = 160)  
    Checksymptoms4 = Checkbutton (tab2, text="Tiredness/Penat", takefocus = 0).place(x = 150, y = 180) 
    Checksymptoms5 = Checkbutton (tab2, text="Nasal Congestion/Hidung Tersumbat", takefocus = 0).place(x = 150, y = 200) 
    Checksymptoms6 = Checkbutton (tab2, text="Runny Nose/Hidung Berair",takefocus = 0).place(x = 150, y = 220) 
    Checksymptoms7 = Checkbutton (tab2, text="Aches and Pains/sakit-sakit badan",takefocus = 0).place(x=150 ,  y = 240) 
    btnSave = Button(tab2,text='Save',command=submitForm)
    btnSave.place(x= 150, y=260)
    btnSubmit = Button(tab2,text='Submit',command=risk)
    btnSubmit.place(x=190, y=260)
    btnClear= Button(tab2,text="Clear",command=clearTab2)
    btnClear.place(x=240,y=260)
#database(tab3)

    btnShowAll = Button(tab3, text="Show All", command=showExisting)
    btnShowAll.grid(column=1,row=0)

    lfExistingAttendance = LabelFrame(tab3, text="My Existing Attendance", bg="white", width=400, height=500)
    lfExistingAttendance.grid(row=1, column=1)

    lblExId = Label(lfExistingAttendance, text="Id")
    lblExId.grid(row=2,column=0,padx=2,sticky=W)
    lblExName = Label(lfExistingAttendance, text="Name")
    lblExName.grid(row=2,column=1,padx=2,sticky=W)
    lblExProgram = Label(lfExistingAttendance, text="Program")
    lblExProgram.grid(row=2,column=2,padx=2,sticky=W)
    lblExMatric = Label(lfExistingAttendance, text="Matric")
    lblExMatric.grid(row=2,column=3,padx=2,sticky=W)
    lblExPhone = Label(lfExistingAttendance, text="Phone")
    lblExPhone.grid(row=2,column=4,padx=2,sticky=W)
    lblExTemp= Label(lfExistingAttendance, text="Body Temperature")
    lblExTemp.grid(row=2,column=5,padx=2,sticky=W)


#button to next page and its grid
btn = Button(root, text="Let's Get Started",bg="black",fg="white",font=("starline",14),command=createsecWindow)
btn.grid(column=0,row=5)

img= ImageTk.PhotoImage(Image.open("covid.png"))
imgDisplay=Label(root, image=img,bg="IndianRed3")
imgDisplay.grid(column=0, row=6)
img1= ImageTk.PhotoImage(Image.open("image.jpg"))
imgDisplay=Label(root, image=img1,bg="IndianRed3")
imgDisplay.grid(column=0, row=7)


#This will loop the application until the user ends it
root.mainloop()