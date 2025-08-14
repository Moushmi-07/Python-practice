import mysql.connector
mydb=mysql.connector.connect(host='',user='root',passwd='1234')
mycursor=mydb.cursor()
mycursor.execute('create database trial')
mycursor.execute('use trial1')
mycursor.execute('create table details(name char(25),class int, rollno int)')
#mycursor.execute('desc details')
#mycursor.execute('insert into details values("moushmi",12,123),("sai krithika",12,1234),("shresthi",12,12345)')
##sql='insert into details(name,class,rollno) values(%s,%s,%s)'
##rows=[('xyz',12,678),('abc',11,1234)]
##mycursor.executemany(sql,rows)
##mydb.commit()
##sql='select * from details'
##
##
##mycursor.execute(sql)
##rows2=mycursor.fetchall()
##for i in rows2:
##    print(i)
##
##
###for i in rows:
##    #print(i[0])
mydb.commit()
mydb.close()
