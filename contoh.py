import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
root = Tk() 
root.geometry("300x200") 
  
w = Label(root, text ='GeeksForGeeks', font = "50")  
w.pack() 
  
messagebox.showinfo("Information", "Your Temperature is Normal") 
messagebox.showinfo("Information", "Your Temperature is Attention need to be given")
messagebox.showinfo("Information", "Your Temperature is Medicine from docter is needed")


frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="", bg="red")
label1.place(x=1, y=1)


label2 = tk.Label(master=frame, text="Your tempretu is okey", bg="blue")
label2.place(width=155, height=115)

window.mainloop()






from tkinter import * 
from tkinter import messagebox 
  
root = Tk() 
root.geometry("300x200") 
  
w = Label(root, text ='GeeksForGeeks', font = "50")  
w.pack() 
  
result = tkMessageBox.askyesno("Python","Would you like to save the data?")
print (result)

root.mainloop()