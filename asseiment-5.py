from unittest import result
import pymysql
import ass2database

mydb=pymysql.connect(host="localhost",user="root",password="",database="ass-2")
mycursor=mydb.cursor()


menu="""
1) Banker
2) customer
"""
status=True
p_status=True

while status:
    print(menu)

choice=int(input("enter your choice :"))
if choice==1:
    print("welcome to Banker page")
    
view="""
1)Register
2)login
3)update customer
4)view customer
5)delet customer
"""

while p_status:
    print(view)
    choice=int(input("enter your choice:"))

    if choice==1:
        email=input("enter e-mail :")
        fname=input("enter first name :")
        lname=input("enter last name :")
        password=input("enter password :")

        print(" you register succesfuly")

        qurey="insert into pras23(email,fname,laname,password)values('%s','%s','%s','%s')"
        args=(email,fname,lname,password)
        mycusor.execute(query % args)
        result=mycursor.fetchone()
        mydb.commit()

        if result:
            print("login successfully")
        else:
            print("enter valid emil or password")
    elif choice==3:
        id=int(input("enter id :"))
        email=input("enter email :")
        fname=input("enter your first name :")
        lname=input("enter your first name :")
        password=input(" enter your password")

        query="update pras23 set email ='%s',fname='%s',lname='%s',password='%s' where id =%s"
        args=(email,fname,lname,password,id)
        mycursor.execute(query % args)
        mydb.commit()
        print("update succesfully !!")


    elif choice==4:
        query="select * frompras23"
        mycursor.execute(query)
        data=mycursor.fetchall()
        print(data)

    elif choice==5:
        id=int(input("enter id :"))
        query="delete from pras23 where id=%s"
        args=(id)
        mycursor.execute(query%args)
        mydb.commit()
        print("deleted succesfully")

choice=input("are you wnt to do more opthion y or n")
if choice=="n" or choice=="N":
    p_status=False

else:
    print("welcome to customer ")
    viewc="""
1) register
2)login
3)withdraw amount
4)deposit Amount
5)view balance
"""
while p_status:
    print(viewc)
    choice=int(input("enter your choice :")
               if choice==1:
               ac_no=int(input("enter account :"))
               cfname=input("enter first name :")
               clname=input("enter last name :")
               cpassword=input("enter password :")
               bal=int(input("enter balane :")
                       print("you register succesfully")
                       query=""insert into cust23(ac_no,cfname,clanme,cpassword,balance) values('%s','%s','%s','%s')
                       args=(ac_no,cfname,clname,cpassword,bal)
                       mucursor.execute(query%args)
                       mydb.commit()
              elif choice==2:
                ac_no=int(input("enter account no :"))
                cpasseord=input("enter password :")
                query="select * from cust23 where ac_no ='%s' and cpassword ='%s'"
                args=(ac_no,cpassword)
                mycursor.execute(query %args)
                result=mycursor.fetchone()
                mydb.commit()
             if result:
                 print("login succesfully")
             else:
                 print("enter void ac num or password")
            elif choice==3:
                ac_no=int(input("enter account no :"))
                cpasseord=input("enter password :")
            
            query="select * from cust23 where ac_no ='%s' and cpassword ='%s'"
            args=(ac_no,cpassword)
            mycursor.execute(query %args)
            result=mycursor.fetchone()
            print("=====>>>result",result)
            print("=====>>>result",result[7])
            mydb.commit()
            if result:
               withdrawamt=int(input("enter withdraw amount :"))

               query="update cust23 set withdrawant ='%s' and where ac_no ='%s'"
               args=(withdrawant,ac_no)
               mycursor.execute(query %args)
               mydb.commit()


               print("your withdraw amount :",withdrawant)


               print("you withdraw successfuly")
               bal=result[7]
               clearbalance=bal-withdrawant
               print("===>> clear balance :",clearbalance)
               query="update cust23 set withdrawant ='%s',clearbalance='%s',balance='%s' where ac_no ='%s'"
               args=(withdrawant,ac_no,clearbalance,bal)
               mycursor.execute(query %args)
               mydb.commit()


            else:
                prin("please enter valid account numb or password !!")


            elif choice==4:
                ac_no=int(input("enter account no :"))
                cpasseord=input("enter password :")
                
                query="select * from cust23 where ac_no ='%s' and cpassword ='%s'"
                args=(ac_no,cpassword)
                mycursor.execute(query %args)
                result=mycursor.fetchone()
                mydb.commit()
                 if result:
                     depositamt=int(input("enter diposit amount :"))
                     query="update cust23 set depositmat=%s where ac_no ='%s'"
                     args=( depositamt,ac_no)
                     mycursor.execute(query %args)
                     mydb.commit()


               print("your withdraw amount :",depositamt)
               print("you withdraw successfuly")

               
               bal=result[7]
               clearbalance=bal-withdrawant
               print("===>> clear balance :",clearbalance)
               query="update cust23 set withdrawant ='%s',clearbalance='%s',balance='%s' where ac_no ='%s'"
               args=(withdrawant,ac_no,clearbalance,bal)
               mycursor.execute(query %args)
               mydb.commit()


               else:
                   print("please enter valid account numb or password !!")

            
            elif choice==5:
                ac_no=int(input("enter account no :"))
                cpasseord=input("enter password :")

                query="select * from cust23 where ac_no ='%s' and cpassword ='%s'"
                args=(ac_no,cpassword)
                mycursor.execute(query %args)
                result=mycursor.fetchone()
                mydb.commit()

                if result:
                    withdrawant=rent[5]
                    deposite=result[6]
                    bal=[7]
                    clearbal=bal+depositmant-withdrawant

                    print("your clear ba;ance is :",clearbal)

                else:
                    print("please enter valid acnum or password !!")

                


                
                 


        

    

            


            
                           
        
        
        
        
         


    
