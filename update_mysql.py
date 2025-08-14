import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123',database='trial')
mycursor=mydb.cursor()
sql='update details set name="mknhjhvgdc" where name="xyz"'
mycursor.execute(sql)
mydb.commit()
sql='select * from details'
mycursor.execute(sql)
rows=mycursor.fetchall()
for i in rows:
    print(i)
mydb.close()
