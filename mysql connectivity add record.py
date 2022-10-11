import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="mandvi",
                             auth_plugin='mysql_native_password',
                             database="school")
print(mydb)
mycursor=mydb.cursor()
ch='y'
while(ch=='y' or ch=='Y'):
    
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    name=input("Enter the Name: ")
    L.append(name)
    age=int(input("Enter Age of Student : "))
    L.append(age)
    class1=input("Enter the Class : ")
    L.append(class1)
    city=input("Enter the City of the Student : ")
    L.append(city)
    stud=(L)
    sql="insert into student (roll,name,age,class,city) values (%s,%s,%s,%s,%s)"
    mycursor.execute(sql,stud)
    mydb.commit()
    ch=(input("Do you want to add more records(y/n):"))    