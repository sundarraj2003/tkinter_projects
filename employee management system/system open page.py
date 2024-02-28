from tkinter import *
from tkinter import ttk
from db import Database
from tkinter import messagebox
root=Tk()
root.title("Employee Management System")
root.config(bg='#2c3e50')
root.geometry("1366x768+0+0")
db=Database("pythonsql")
#Root variables:
name=StringVar()
age=StringVar()
doj=StringVar()
email=StringVar()
gender=StringVar()
contact=StringVar()

entries_frame=Frame(root,bg="#535C68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management System",font=('calibri',18,'bold'),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20,sticky="w")
lblName=Label(entries_frame,text="Name",font=("calibri",16),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName=Entry(entries_frame,textvariable=name,font=("calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lblAge=Label(entries_frame,text="Age",font=('calibri',16),bg="#535c68",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtAge=Entry(entries_frame,textvariable=age,font=("calibri",16),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky='w')

lblDoj=Label(entries_frame,text="D.O.J",font=("Calibri",16),bg="#535c68",fg="white")
lblDoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtDoj=Entry(entries_frame,textvariable=doj,font=("calibri",16),width=30)
txtDoj.grid(row=2,column=1,padx=10,pady=10,sticky='w')

lblEmail=Label(entries_frame,text="Email",font=('calibri',16),bg="#535c68",fg="white")
lblEmail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtEmail=Entry(entries_frame,textvariable=email,font=('calibri',16),width=30)
txtEmail.grid(row=2,column=3,padx=10,pady=10,sticky='w')

lblgender=Label(entries_frame,text="Gender",font=("calibri",16),bg="#535c68",fg="white")
lblgender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
txtGender=ttk.Combobox(entries_frame,textvariable=gender,font=("calibri",16),width=28,state="readonly")
txtGender['values']=('Male','Female')
txtGender.grid(row=3,column=1,padx=10,pady=10,sticky="w")

lblContact=Label(entries_frame,text="Contact",font=("calibri",16),bg="#535c68",fg="white")
lblContact.grid(row=3,column=2,padx=10,pady=10,sticky='w')
txtContact=Entry(entries_frame,textvariable=contact,font=("calibri",16),width=30)
txtContact.grid(row=3,column=3,padx=10,pady=10,sticky="w")

lblAddress=Label(entries_frame,text="Address",font=("calibri",16),bg="#535c68",fg="white")
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky='w')

txtAddress=Text(entries_frame,font=("calibri",16),width=85,height=5)
txtAddress.grid(row=5,column=0,padx=10,columnspan=4,sticky='w')
#Functions
def getdata(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data['values']
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0,END)
    txtAddress.insert(END,row[7])

def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
def add_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtDoj.get() == "" or txtEmail.get()=="" or txtGender.get()=="" or txtContact.get()=="" or  txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error in input","Please fill the all Details!!!")
        return
    db.insert(txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),txtGender.get(),txtContact.get(),txtAddress.get(1.0,END))
    messagebox.showinfo("Success","Record Inserted")
    clearAll()
    displayall()

def update_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtDoj.get() == "" or txtEmail.get()=="" or txtGender.get()=="" or txtContact.get()=="" or  txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error in input","Please fill the all Details!!!")
        return
    db.update(txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),txtGender.get(),txtContact.get(),txtAddress.get(1.0,END),row[0])
    messagebox.showinfo("Success","Record update")
    clearAll()
    displayall()

def delete_employee():
    db.remove(row[0])
    clearAll()
    displayall()

def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    email.set("")
    gender.set("")
    contact.set("")
    txtAddress.delete(1.0,END)

#Buttons
btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")

btnAdd=Button(btn_frame,command=add_employee,text="Add Details",font=("calibri",16,"bold"),width=15,fg="white",bg="#16a085",bd=0).grid(row=0,column=0)

btnEdit=Button(btn_frame,command=update_employee,text="Update Details",font=("calibri",16,"bold"),width=15,fg="white",bg="#2980b9",bd=0).grid(row=0,column=1,padx=10)

btnDelete=Button(btn_frame,command=delete_employee,text="Delete Details",font=("calibri",16,"bold"),width=15,fg="white",bg="#c0392b",bd=0).grid(row=0,column=2,padx=10)

btnClear=Button(btn_frame,command=clearAll,text="Clear Details",font=("calibri",16,"bold"),width=15,fg="white",bg="#f39c12",bd=0).grid(row=0,column=3,padx=10)


#Table frames
tree_frame=Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=480,width=1366,height=500)
style=ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",18),rowheight=50) #modified the font of the body
style.configure("mystyle.Treeview.Heading",font=("calibri",18))#modified the font of heading
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=5)
tv.heading("2",text="NAME")
tv.heading("3",text="AGE")
tv.column("3",width=5)
tv.heading("4",text="D.O.B")
tv.column("4",width=10)
tv.heading("5",text="EMAIL")
tv.heading("6",text="GENDER")
tv.column("6",width=10)
tv.heading("7",text="CONTACT")
tv.column("7",width=40)
tv.heading("8",text="ADDRESS")
tv['show']="headings"
tv.pack(fill=X)
tv.bind("<ButtonRelease-1>",getdata)
displayall()
root.mainloop()