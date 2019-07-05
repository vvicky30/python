#!/usr/bin/python3

import mysql.connector as mysql
#RDS info
u='root'  #master user-name
p='------------'  #master password
db='adhocnetworks'  #database-name
h='------------------------rds.amazonaws.com'  #endpoint-adresss of rds-server


#now conecting
conn=mysql.connect(user=u,password=p,database=db,host=h)

#now generating a sequel(sql) language cursor
cur=conn.cursor()


#now we can write sql-query
cur.execute("show tables;")

#now printing result:---
print(cur.fetchall())

#closing connections
conn.close()
