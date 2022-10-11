import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="mandvi",
                             auth_plugin='mysql_native_password',
                             database="school")
print(mydb)
mycursor=mydb.cursor()
mycursor.execute("SELECT*FROM student ORDER BY roll")
mydb.commit()
