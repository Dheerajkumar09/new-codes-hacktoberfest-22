import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="mandvi",
                             auth_plugin='mysql_native_password',
                             database="school")
print(mydb)
mycursor=mydb.cursor()
s=int(input("Enter roll no to search: "))
rl=(s,)
sql="select * from student where roll=%s"
mycursor.execute(sql,rl)
res=mycursor.fetchall()
print("The Students details are as follows : ")
print("(Roll, Name, Age, Class, City)")
for x in res:
    print(x)
    