import os
import platform
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database='parking') 
mycursor=mydb.cursor()
defAdd_Record():
    L=[]
    id1=int(input("Enter the parking number : "))
L.append(id1)
    pname1=input("Enter the Parking Name: ")
L.append(pname1)
    level1=input("Enter level of parking : ")
L.append(level1)
    freespace1=input("Is there any freespace or not :YES/NO ")
L.append(freespace1)
    vehicleno1=input("Enter the Vehicle Number : ")
L.append(vehicleno1)
    nod1=int(input("Enter total number of days for parking: "))
L.append(nod1)
    if nod1==1:
        Payment1=20
elif nod1==2:
         Payment1=40
elif nod1==3:
         Payment1=60
elif nod1==4:
          Payment1=80
elif nod1==5:
          Payment1=100
elif nod1==6:
           Payment1=120

L.append(Payment1)
    stud=(L)
sql='insert into parkmaster12(pid,pnm,level,freespace,vehicleno,nod,payment) values(%s,%s,%s,%s,%s,%s,%s)'
mycursor.execute(sql,stud)
mydb.commit()
defRec_View():
print("Select the search criteria : ")
print("1. Parking Number")
print("2. Parking Name")
print("3. Level No")
print("4. All")
ch=int(input("Enter the choice : "))
    if ch==1:
       s=int(input("Enter Parking no : "))
rl=(s,)
sql="select * from parkmaster12 where pid=%s"
mycursor.execute(sql,rl)
       res=mycursor.fetchall()
elifch==2:
       s=input("Enter Parking Name : ")
rl=(s,)
sql="select * from parkmaster12 where pnm=%s"
mycursor.execute(sql,rl)
       res=mycursor.fetchall()
elifch==3:
       s=int(input("Enter Level of Parking : "))
rl=(s,)
sql="select * from parkmaster12 where level=%s"
mycursor.execute(sql,rl)
       res=mycursor.fetchall()
elifch==4:
sql="select * from parkmaster12"
mycursor.execute(sql)
       res=mycursor.fetchall()
print("Details about Parking are as follows : ")
print("(Parking Id,ParkingName,Level,FreeSpace(Y/N),Vehicle No,No of days for parking,Payment)")
    for x in res:
        print(x)
print('Task comple ted')
defVehicle_Detail():
    L=[]
    vid1=int(input("Enter Vehicle No : "))
L.append(vid1)
    vnm1=input("Enter Vehicle Name/Model Name : ")
L.append(vnm1)
    dateofpur1=input("Enter Year-Month-date of purchase : ")
L.append(dateofpur1)
vdt=(L)
sql="insert into vehicle(pid,vnm,dateofpur) values(%s,%s,%s)"
mycursor.execute(sql,vdt)
mydb.commit()
defVehicle_View():   
    vid1=int(input("Enter the vehicle number of the vehicle whose details is to be viewed : "))
sql='select parkmaster12.pid,parkmaster12.pnm,parkmaster12.vehicleno, vehicle.pid,vehicle.vnm from parkmaster12 INNER JOIN vehicle ON parkmaster12.pid=vehicle.pid and vehicle.pid=%s'  
rl=(vid1,)
print('The following are the detailes you wanted:')
mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    for x in res:
        print(x)
print('Task compelted')
defremove():
    vid1=int(input("Enter the vehicle number of the vehicle to be deleted : "))
rl=(vid1,)
sql="Delete from vehicle where pid=%s"
mycursor.execute(sql,rl)
mydb.commit()
print('Removed as per the command')
defMenu():
print("Enter 1 : To Add Parking Detail")
print("Enter 2 : To View Parking Detail ")
print("Enter 3 : To Add Vehicle Detail ")
print("Enter 4 : To Remove Vehicle Record")
print("Enter 5 : To see the details of Vehicle")
input_dt = int(input("Please Select An Above Option: "))
if(input_dt== 1):
Add_Record()
elif (input_dt==2):
Rec_View()
elif (input_dt==3):
Vehicle_Detail()
elif (input_dt==4):
remove()
elif (input_dt==5):
Vehicle_View()
    else:
print("Enter correct choice....")
Menu()
defrunAgain():
runAgn=input('\nwant to run Again Y/n:')
    while(runAgn.lower()=='y'):
        if(platform.system()=='Windows'):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
Menu()
runAgn=input('\nwant to run Again Y/n:')      runAgain()
