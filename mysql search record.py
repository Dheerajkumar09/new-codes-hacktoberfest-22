import mysql.connector
mydb=mysql.connector.connect(your login credentials)
print(mydb)
mycursor=mydb.cursor()
no=(input("Enter no to be searched : "))
rl=(no,)
sql="select * from record where no=%s"
mycursor.execute(sql,rl)
res=mycursor.fetchall()
print("The student details are as follows : ")
print("(NO, NAME , AGE, DEPARTMENT, FEE,SEX)")
for x in res:
    print(x)
