import mysql.connector
mydb=mysql.connector.connect(host="localhost",
     user="root",passwd="mandvi",database="flight"
     ,auth_plugin='mysql_native_password')
print(mydb)
mycursor=mydb.cursor()
ch='y'
while (ch=='y' or ch=='Y'):
    L=[]
    flno=(input("Enter the flight number : "))
    L.append(flno)
    start=input("Enter the start: ")
    L.append(start)
    end=(input("Enter end : "))
    L.append(end)
    no_flight=int(input("Enter no.of flights : "))
    L.append(no_flight)
    air=input("Enter the airline name : ")
    L.append(air)
    fare=input("Enter fare : ")
    L.append(fare)
    stud=(L,)
    sql="insert into flight (flno,start,end,no_flight,air,fare) values (%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,stud)
    mydb.commit()
    ch=input("Do you want to add more record(y/n):")