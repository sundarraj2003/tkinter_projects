from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="raj17122003",database="managementsystem")

def insert(name,age,city):
    res=con.cursor()
    sql="insert into employee (name,age,city) values(%s,%s,%s)"
    user=(name,age,city)
    res.execute(sql,user)
    con.commit()

def update(name,age,city,id):
    res=con.cursor()
    sql="Update employee set name=%s,age=%s,city=%s where id=%s"
    user=(name,age,city,id)
    res.execute(sql,user)
    con.commit()
def select():
    res=con.cursor()
    sql="Select id,name,age,city from employee"
    res.execute(sql)
    result=res.fetchall()
    #print(result)
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))
    con.commit()
def delete(id):
    res=con.cursor()
    sql="delete from employee where id=%s"
    user=(id,)
    res.execute(sql,user)
    con.commit()
while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        name=input("Enter Name:")
        age=input("Enter Age:")
        city=input("Enter City:")
        insert(name,age,city)
        print("Insert Is Successfully")
    elif choice==2:
        id=input("Enter the Id:")
        name=input("Enter Name:")
        age=input("Enter Age:")
        city=input("Enter City:")
        update(name,age,city,id)
    elif choice==3:
        select()
    elif choice==4:
        id=input("Enter the Id to Delete:")
        delete(id)
    elif choice==5:
        quit()
    else:
        print("Invalid Selection...Please Try Again")