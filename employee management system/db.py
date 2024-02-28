import mysql.connector
class Database:
    def __init__(self,db):
        self.con=mysql.connector.connect(host="localhost",user="root",password="raj17122003",database=db)
        self.cur=self.con.cursor()
        sql="""CREATE TABLE IF NOT EXISTS employees(
        id integer primary key auto_increment,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text
        )"""
        self.cur.execute(sql)
        self.con.commit()
    #Insert Function
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert employees(name,age,doj,email,gender,contact,address) values (%s,%s,%s,%s,%s,%s,%s)",(name,age,doj,email,gender,contact,address))
        self.con.commit()

    #fetchall
    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows=self.cur.fetchall()
        #print(rows)
        return rows

    def remove(self,id):
        self.cur.execute("delete from employees where id=%s",(id,))
        self.con.commit()

    #update a Record in Db
    def update(self,name,age,doj,email,gender,contact,address,id):
        self.cur.execute("update employees set name=%s,age=%s,doj=%s,email=%s,gender=%s,contact=%s,address=%s where id=%s",(name,age,doj,email,gender,contact,address,id))
        self.con.commit()
        print("Update Successfully")


a=Database("pythonsql")
a.fetch()