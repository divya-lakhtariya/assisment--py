import pymysql

mydb=pymysql.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()

mycursor.execute("create data base if not exists ass-2")
mydb.commit()

mydb=pymysql.connect(host="localhost",user="root",password="",database="ass-2")
mycursor=mydb.cursor()

mycursor.execute("creat table if not exists pras23(id int primarykey auto_increment,fname varchar(20),lname varchar(20),email varchar(20),password varchar(20))")
mydb.commit()

mycursor.execute("creat table if not exists pras23(id int primarykey auto_increment,fname varchar(20),lname varchar(20),email varchar(20),password varchar(20))")
mydb.commit()
