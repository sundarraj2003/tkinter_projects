from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from tkcalendar import DateEntry
from datetime import datetime
from time import strftime

import sqlite3
import random

#Frond Page of Ticket System
frond=Tk()
frond.geometry('700x700')
frond.configure(background='#D3D3D3')
frond.title("Parking Lot Management System")

#Database connectivity
conn=sqlite3.connect('ticket_booking.db')
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ticket (name TEXT,vehicle_no TEXT,vehicle_type,ticket_id TEXT PRIMARY KEY,ticket_date TEXT,ticket_Exit_date TEXT DEFAULT \"NOT EXIT\")")


#Fetching all Details
cursor.execute("SELECT * FROM ticket")
tickets=cursor.fetchall()

#getting all ticket id

tickets_id=[]
for i in tickets:
    tickets_id.append(i[1])

conn.commit()

#Backend
#Backend functions

#Error Message Function

def show_message(title,message):
    messagebox.showerror(title,message)

#Generate Ticket
def random_ticket_id():
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return ''.join(random.choice(letters) for i in range(10))

#Enter The Ticket Function
def Booking():
    book=Tk()
    book.geometry('700x400')
    book.title('Book Ticket')
    book.configure(background='#D3D3D3')
    
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    name=StringVar(book)
    vehicle_no=StringVar(book)
    ticket_date=StringVar(book)
    ticket_date.set(current_date_time)
    vehicle_type=StringVar(book)
    
    ticket_id=StringVar(book)
    ticket_Exit_date=StringVar(book)

    while True:
        global tickets_id
        t_id=random_ticket_id()
        if t_id not in tickets_id:
            ticket_id.set(random_ticket_id())
            break
        continue
 
    def BookNow():
        if len(name.get())<2 or len(vehicle_no.get())<5 or vehicle_type.get()=="":
            show_message('Error', 'Enter valid details')
            return
        try:
            conn=sqlite3.connect('ticket_booking.db')
            cursor=conn.cursor()
            cursor.execute("INSERT INTO ticket (name,vehicle_no,vehicle_type,ticket_id,ticket_date) VALUES (?, ?, ?, ?,?)", (str(name.get()), str(vehicle_no.get()), str(vehicle_type.get()), str(ticket_id.get()),str(ticket_date.get())))
            conn.commit()
            show_message('Successful', 'Your booking is successful, your ticket id is {}'.format(ticket_id.get()))
            book.destroy()
        except sqlite3.Error as e:
            show_message('Error', e)
        finally:
            conn.close()
   
    Label(book, text='Enter details',justify='center', font=('Arial', 20)).grid(row=0, column=0, padx=250, pady=10, columnspan=2,sticky='ew')
    
    Label(book, text='Name', font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky='e')
    Entry(book, textvariable=name,width=20).grid(row=1, column=1,sticky='w')
    
    Label(book, text='Ticket Id', font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky='e')
    Entry(book, textvariable=ticket_id, state='disabled').grid(row=2, column=1,sticky='w')
    
    Label(book, text='Vechicle No', font=('Arial', 12)).grid(row=3, column=0, padx=10, sticky='e', pady=10)
    Entry(book, textvariable=vehicle_no).grid(row=3, column=1,sticky='w')

    Label(book, text='Vechicle Type', font=('Arial', 12)).grid(row=4, column=0, padx=10, sticky='e', pady=10)
    vehicle_combobox =ttk.Combobox(book, values=["Car", "Truck", "Motorcycle", "Bicycle"],textvariable=vehicle_type,state="readonly")
    vehicle_combobox.grid(row=4,column=1,sticky='w')

    
    Label(book, text='Entry Date', font=('Arial', 12)).grid(row=5, column=0, padx=10, pady=10, sticky='e')
    Entry(book,textvariable=ticket_date).grid(row=5, column=1,sticky='w')
    
    Button(book, text='Confirm', bg='green', fg='white',justify='center', font=('Arial', 17), width=9, command=lambda:BookNow()).grid(row=6, columnspan=2, pady=20,sticky='s')
    book.mainloop()
   
    #View Function
def ViewHistory():
    
    view= Tk()
    view.geometry('1110x600+50+50')
    view.title('View Ticket Booking History')
    view.configure(background="#F2F2F2")
    
    Label(view, text='Customer Name', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=0, pady=10)
    Label(view, text='Vechicle No', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=1, pady=10)
    Label(view, text='Vechicle Type', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=2, pady=10)
    Label(view, text='Ticket ID', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=3, pady=10)
    Label(view, text='Entry Time', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=4, pady=10)
    Label(view, text='Exit Time', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=5, pady=10)
    conn = sqlite3.connect('ticket_booking.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ticket')
    tickets = cursor.fetchall()
    for i in range(len(tickets)):
        Label(view, text=tickets[i][0], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, column=0)
        Label(view, text=tickets[i][1], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=1)
        Label(view, text=tickets[i][2], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=2)
        Label(view, text=tickets[i][3], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=3)
        Label(view, text=tickets[i][4], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=4)
        Label(view, text=tickets[i][5], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=5)
                        
    view.mainloop()
    view.after(300,ViewHistory)
    conn.close()

#Delete function
def DeleteBooking():
    
    Delete = Tk()
    Delete.geometry('1250x600+50+50')
    Delete.title('View Ticket Booking History')
    Delete.configure(background='#D3D3D3')
    
    Label(Delete, text='Customer Name', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=0, pady=10)
    Label(Delete, text='Vechicle No', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=1, pady=10)
    Label(Delete, text='Vechicle Type', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=2, pady=10)
    Label(Delete, text='Ticket ID', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=3, pady=10)
    Label(Delete, text='Entry Time', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=4, pady=10)
    Label(Delete, text='Exit Time', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=5, pady=10)
    Label(Delete, text='Delete', font=('Arial', 12), borderwidth=1, relief="solid", width=20).grid(row=0, column=6, pady=10)

    
    def delete_rows(ticket_id):
        try:
            conn = sqlite3.connect("ticket_booking.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ticket WHERE ticket_id = ?", (ticket_id,))
            conn.commit()
            show_message('Success', 'Ticket deleted')
            conn.close()
        except sqlite3.Error as e:
            show_message('Sqlite error', e)
        finally:
            conn.close()
    conn = sqlite3.connect('ticket_booking.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ticket')
    tickets = cursor.fetchall()
    for i in range(len(tickets)):
        Label(Delete, text=tickets[i][0], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, column=0)
        Label(Delete, text=tickets[i][1], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=1)
        Label(Delete, text=tickets[i][2], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=2)
        Label(Delete, text=tickets[i][3], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=3)
        Label(Delete, text=tickets[i][4], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=4)
        Label(Delete, text=tickets[i][5], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=5)
        Button(Delete, text='Delete', command=lambda current_id=tickets[i][3]:( delete_rows(current_id),Delete.destroy()),width=15, bg='#FFA07A', fg='#FFFFFF').grid(padx=5,row=i+1, column=6,sticky="w")
    Delete.mainloop()
    

    conn.close()

#Exit Entry Function
def ExitBooking():
    
    Exit = Tk()
    Exit.geometry('1250x600+50+50')
    Exit.title('Exit Entry Form')
    Exit.configure(background='#D3D3D3')
    
    Label(Exit, text='Customer Name', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=0, pady=10)
    Label(Exit, text='Vechicle No', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=1, pady=10)
    Label(Exit, text='Vechicle Type', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=2, pady=10)
    Label(Exit, text='Ticket ID', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=3, pady=10)
    Label(Exit, text='Entry Time', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=4, pady=10)
    Label(Exit, text='Exit Time', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=5, pady=10)
    Label(Exit, text='Enter Exit', font=('Arial', 12), borderwidth=1, relief="solid", width=20,bg="#F2F2F2",fg= "#333333").grid(row=0, column=6, pady=10)

    
    def Exit_Entry(ticket_id):
        try:
            conn = sqlite3.connect("ticket_booking.db")
            cursor = conn.cursor()
            current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            cursor.execute("UPDATE ticket SET ticket_Exit_date=? WHERE ticket_id = ?", (str(current_date_time),ticket_id,))
            conn.commit()
            show_message('Success', 'Exit The Vechicle')
            conn.close()
        except sqlite3.Error as e:
            show_message('Sqlite error', e)
        finally:
            conn.close()
    conn = sqlite3.connect('ticket_booking.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ticket WHERE ticket_Exit_date="NOT EXIT"')
    tickets = cursor.fetchall()
    for i in range(len(tickets)):
        Label(Exit, text=tickets[i][0], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, column=0)
        Label(Exit, text=tickets[i][1], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=1)
        Label(Exit, text=tickets[i][2], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=2)
        Label(Exit, text=tickets[i][3], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=3)
        Label(Exit, text=tickets[i][4], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=4)
        Label(Exit, text=tickets[i][5], borderwidth=1, relief="solid", width=20,bg="#ECECEC",fg= "black").grid(row=i+1, padx=10, column=5)
        Button(Exit, text='Exited', command=lambda current_id=tickets[i][3]: (Exit_Entry(current_id),Exit.destroy()),width=15,bg="#FFA500",fg="#FFFFFF").grid(padx=5,row=i+1, column=6,sticky="w")
    Exit.mainloop()
    

    conn.close()

#Define Heading

frond_title=Label(frond, text='Ticket Management System',bg='#ADD8E6', font=('Arial', 20))
frond_title.grid(row=0, column=0, columnspan=2, padx=170, pady=30,sticky="w")


#Defining buttons
Button(frond, text='Entry Booking', font=('Arial', 16), command=lambda:Booking(), width=20, height=2,bg='#F5F5F5', fg='#000000').grid(row=1, padx=200, pady=20,sticky="w")

Button(frond, text='View History', font=('Arial', 16), command=lambda:ViewHistory(), width=20, height=2,bg='blue', fg='white').grid(row=2,padx=200, pady=20,sticky="w")

Button(frond, text='Delete Booking', font=('Arial', 16), command=lambda:DeleteBooking(), width=20, height=2, bg='#FFA07A', fg='#FFFFFF').grid(row=3,padx=200, pady=20,sticky="w")

Button(frond, text='Entry Exit', font=('Arial', 16) , command=lambda:ExitBooking(), width=20, height=2, bg='#E0FFFF', fg='#000000').grid(row=4, padx=200, pady=20,columnspan=2,sticky="w")

Button(frond, text='Quit', font=('Arial', 18), command=lambda:frond.destroy(), width=20, height=2, bg='#FF6347', fg='#FFFFFF').grid(row=5,padx=140, pady=30,columnspan=2,sticky="nsew")

# mainloop
frond.mainloop()
