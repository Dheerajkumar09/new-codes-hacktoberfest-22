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
    roll=int(input("Enter the roll number of the student to be deleted : "))
    rl=(roll,)
    sql="delete from Student where roll=%s"
    mycursor.execute(sql,rl)
    print('Record deleted!!!')
    mydb.commit()
    ch=(input("Do you want to delete more records(y/n):")) 