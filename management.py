import mysql.connector as ysql

cont1 = ysql.connect(host="localhost", user="root", password="12345", database="Dairy") 
cur = cont1.cursor()

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
selection = int(input("Enter your option= "))

if selection == 1:
    password1 = input("Enter your password= ") 
    cur.execute("SELECT * FROM admindetails") 
    for Adminname, password in cur:
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
            k = int(input("Enter your choice= ")) 

            if k == 1:
                n = int(input("Enter no of items= ")) 
                for _ in range(n):
                    print("-----------------------------------------------------------")
                    pid = int(input("Enter product id= ")) 
                    pname = input("Enter product name= ") 
                    pp = int(input("Enter Product price= ")) 
                    qua = int(input("Enter the quantity= "))

                    cur.execute("INSERT INTO items VALUES (%s, %s, %s, %s)", (pid, pname, pp, qua)) 
                    cont1.commit()
                    print("+ +++++++++Items are successfully added++++++++++")

            elif k == 2:
    # View products
                 print("----------------------------------------------------------")
                 print("Products available:")
                 cur.execute("SELECT * FROM items")
                 products = cur.fetchall()
                 if not products:
                    print("No products available.")
                 else:
                   for product in products:
                      print("Product ID:", product[0])
                      print("Product Name:", product[1])
                      print("Price:", product[2])
                      print("Quantity:", product[3])
                      print("----------------------------------------------")

            
            
            elif k == 3:
                name = input("Enter the name of the product= ")
                p1 = int(input("Enter the price of the product= "))
                cur.execute("UPDATE items SET Productprice=%s WHERE Productname=%s", (p1, name)) 
                cont1.commit()
                print("+++++++++++Changes are done successfully+++++++++++++")

            elif k == 4:
                password2 = input("Enter old password= ")
                password3 = input("Enter password you want= ")
                cur.execute("UPDATE admindetails SET password=%s WHERE password=%s", (password3, password2)) 
                cont1.commit()
                print("+++++++password has been changed successfully+++++++++++++")

            elif k == 5:
                item = input("Enter the name of the item= ")
                quantity = int(input("Enter the quantity= ")) 
                cur.execute("SELECT * FROM items")
                r = cur.fetchall()
                for row in r:
                    if row[1] == item:
                        print("Your generated amount is", row[2] * quantity)
                        break

            elif k == 6:
                print("+++++++++++++Customer's details+++++++++++++")
                cur.execute("SELECT * FROM customerdetails") 
                r = cur.fetchall()
                print(r)

elif selection == 2:
    customername = input("Enter your name= ")
    phoneno = input("Enter your phone number= ")
    Address = input("Enter your address= ")
    cur.execute("INSERT INTO customerdetails VALUES (%s, %s, %s)", (customername, phoneno, Address)) 
    cont1.commit()
    print("++++++++++Welcome to Customer's page++++++++++")
    print("1. Purchase item")
    print("2. View available items")
    g = int(input("Enter your choice- "))

    if g == 1:
        iname = input("Enter the name of the item= ")
        quant = int(input("Enter the quantity= ")) 
        cur.execute("SELECT * FROM items")
        r = cur.fetchall()
        for i in range(len(r)):
            #if r[i][1] == iname:
              #if quant <= r[i][3]:
               # h = r[i][3] - quant
                #cur.execute("UPDATE items SET Quantity = %s WHERE Productname = %s", (h, iname)) 
                cont1.commit()
                cur.execute("INSERT INTO orderdetails VALUES (%s, %s, %s, %s)", (customername, phoneno, Address, quant)) 
                print("+++++++++++++Order has been placed+++++++++++++")
           # else:
               # print("Requested item is unavailable")


    elif g == 2:
        cur.execute("SELECT Productname FROM items")
        r = cur.fetchall()
        print("++++++++++Available items are++++++++++")
        for row in r:
             print(row[0])

cont1.close()
