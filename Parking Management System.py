import os
import platform
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="parking")
mycursor = mydb.cursor()

def Add_Record():
    L = []
    id1 = int(input("Enter the parking number: "))
    L.append(id1)
    pname1 = input("Enter the Parking Name: ")
    L.append(pname1)
    level1 = input("Enter level of parking: ")
    L.append(level1)
    freespace1 = input("Is there any free space (YES/NO): ")
    L.append(freespace1)
    vehicleno1 = input("Enter the Vehicle Number: ")
    L.append(vehicleno1)
    nod1 = int(input("Enter total number of days for parking: "))
    L.append(nod1)

    Payment1 = nod1 * 20  # Assigning payment dynamically based on days
    L.append(Payment1)

    stud = tuple(L)
    sql = "INSERT INTO parkmaster12(pid, pnm, level, freespace, vehicleno, nod, payment) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, stud)
    mydb.commit()
    print("Record Added Successfully!")

def Rec_View():
    print("Select the search criteria: ")
    print("1. Parking Number")
    print("2. Parking Name")
    print("3. Level No")
    print("4. All")
    
    ch = int(input("Enter the choice: "))

    if ch == 1:
        s = int(input("Enter Parking no: "))
        rl = (s,)
        sql = "SELECT * FROM parkmaster12 WHERE pid=%s"
    elif ch == 2:
        s = input("Enter Parking Name: ")
        rl = (s,)
        sql = "SELECT * FROM parkmaster12 WHERE pnm=%s"
    elif ch == 3:
        s = input("Enter Level of Parking: ")
        rl = (s,)
        sql = "SELECT * FROM parkmaster12 WHERE level=%s"
    elif ch == 4:
        sql = "SELECT * FROM parkmaster12"
        mycursor.execute(sql)
        res = mycursor.fetchall()
        print("Details about Parking: ")
        print("(Parking Id, Parking Name, Level, Free Space, Vehicle No, No of days, Payment)")
        for x in res:
            print(x)
        return
    else:
        print("Invalid Choice")
        return

    mycursor.execute(sql, rl)
    res = mycursor.fetchall()
    
    print("Details about Parking: ")
    print("(Parking Id, Parking Name, Level, Free Space, Vehicle No, No of days, Payment)")
    for x in res:
        print(x)

def Vehicle_Detail():
    L = []
    vid1 = int(input("Enter Vehicle No: "))
    L.append(vid1)
    vnm1 = input("Enter Vehicle Name/Model Name: ")
    L.append(vnm1)
    dateofpur1 = input("Enter Year-Month-Date of purchase: ")
    L.append(dateofpur1)

    vdt = tuple(L)
    sql = "INSERT INTO vehicle(pid, vnm, dateofpur) VALUES (%s, %s, %s)"
    mycursor.execute(sql, vdt)
    mydb.commit()
    print("Vehicle Record Added Successfully!")

def Vehicle_View():
    vid1 = int(input("Enter the vehicle number to view details: "))
    sql = """SELECT parkmaster12.pid, parkmaster12.pnm, parkmaster12.vehicleno, 
             vehicle.pid, vehicle.vnm FROM parkmaster12 
             INNER JOIN vehicle ON parkmaster12.pid = vehicle.pid 
             WHERE vehicle.pid = %s"""
    
    rl = (vid1,)
    mycursor.execute(sql, rl)
    res = mycursor.fetchall()
    
    print("The following are the details:")
    for x in res:
        print(x)

def remove():
    vid1 = int(input("Enter the vehicle number to delete: "))
    rl = (vid1,)
    sql = "DELETE FROM vehicle WHERE pid=%s"
    mycursor.execute(sql, rl)
    mydb.commit()
    print("Vehicle Record Removed Successfully!")

def Menu():
    print("Enter 1: To Add Parking Detail")
    print("Enter 2: To View Parking Detail")
    print("Enter 3: To Add Vehicle Detail")
    print("Enter 4: To Remove Vehicle Record")
    print("Enter 5: To View Vehicle Details")

    input_dt = int(input("Please Select An Option: "))

    if input_dt == 1:
        Add_Record()
    elif input_dt == 2:
        Rec_View()
    elif input_dt == 3:
        Vehicle_Detail()
    elif input_dt == 4:
        remove()
    elif input_dt == 5:
        Vehicle_View()
    else:
        print("Enter a correct choice....")
    
    runAgain()

def runAgain():
    runAgn = input("\nWant to run again? (Y/n): ").strip().lower()
    if runAgn == "y":
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        Menu()

Menu()
