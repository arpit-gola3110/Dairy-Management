import mysql.connector as ysql
cont1 = ysql.connect(host="localhost", user="root", password="12345", database="Dairy") 
cur=cont1.cursor()
if cont1.is_connected():
    print("-++++++++++++++++++++++++++yes!!++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
print("+------------Welcome to dairy management system------------+")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(" ")
print(" ")
print("Select the given option")
print("1. Admin")
print("2. Customer")
print("3. Exit")
selection=int(input("Enter your option= "))
if selection == 1:
    password1 = input("Enter your password= ") 
    cur.execute("select * from admindetails") 
    for i in cur:
        Adminname, password = i
        if password == password1:
            print("--------------------------WELCOME TO ADMIN'S PAGE------------------")
            print("Select from given options")
            print("1. Add products")
            print("2. View products")
            print("3. Change product pricing")
            print("4. Change password")
            print("5. Bill")
            print("6. Customer's log")
            print("7. Exit")
            k=int(input("Enter your choice= ")) 
            if k == 1:
                n = int(input("Enter no of items= ")) 
                for i in range(n):
                    print("-----------------------------------------------------------")
                    pid = int(input("Enter product id= ")) 
                    pname = input("Enter product name= ") 
                    pp = int(input("Enter Product price= ")) 
                    qua = int(input("Enter the quantity= "))

                    cur.execute("insert into items values('"+str(pid)+"', '"+str(pname)+"', '"+str(pp)+"', '"+str (qua)+"')") 
                    cont1.commit()
                    print("+ +++++++++Items are successfully added++++++++++")
            elif k == 3:
                name = input("Enter the name of the product= ")
                p1 = int(input("Enter the price of the product= "))
                cur.execute("update items set Productprice='"+str(p1)+"' where Productname='"+str(name)+"'") 
                cont1.commit()
                print("+++++++++++Changes are done successfully+++++++++++++")
            elif k == 4:
                password2 = int(input("Enter old password= "))
                password3= int(input("Enter password you want= "))
                cur.execute("update admindetails set password= '"+str(password3)+"' where password='"+str(password2)+"'") 
                cont1.commit()
                print("+++++++password has been changed succesfully+++++++++++++")
            elif k == 5:
                item = input("Enter the name of the item= ")
                quantity = int(input("Enter the quantity= ")) 
                cur.execute("select * from items")
                r = cur.fetchall()
                for i in range(len(r)):
                    if r[i][1] == item:
                        print("Your generated amount is", r[i][2] * quantity)
                        h = r[i][3] - quantity
                        cur.execute("update items set Quantity = "+str(h)+" where Productname "+str(item)+"'")
                        cont1.commit()
            elif k == 6:
                print("+++++++++++++Customer's details+++++++++++++")
                cur.execute("select * from customerdetails") 
                cont1.commit()
                r = cur
                print("r")
if selection == 2:
    customername = input("Enter your name=")
    phoneno = int(input("Enter your phone number= "))
    Address = input("Enter your address= ")
    cur.execute("insert into customerdetails values('"+str(customername)+"', '"+str(phoneno)+"','"+str(Address)+"')") 
    cont1.commit()
    print("++++++++++Welcome to Customer's page++++++++++")
    print("1. Purchase item")
    print("2. View available items")
    g= int(input("Enter your choice- "))
    if g == 1:
        iname = input("Enter the name of the item= ")
        quant = int(input("Enter the quantity= ")) 
        cur.execute("select * from items")
        r = cur.fetchall()
        for i in range(len(r)):
                if r[i][1] == iname:
                    if quant <= r[i][3]:
                        h=r[i][3] - quant
                        cur.execute("update items set Quantity = '"+str(h)+" where Productname = '"+str(iname)+"'") 
                        cont1.commit()
                        cur.execute("insert into orderdetails values ("+str(customername)+"', '"+str (phoneno)+"', '"+str(Address)+"','"+str (quant)+"')") 
                        print("+++++++++++++Order has been placed+++++++++++++")
    
                    else:
                        print("Requested item is uvavilable")
    elif g == 2:
        cur.execute("select * from items")
        r = cur.fetchall()
        print("++++++++++Available items are++++++++++")
        for i in range(len(r)):
             print(r[i][1])
