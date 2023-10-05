'''Write a program to load database details into excel sheet.
  - Create a table student in database (regno integer, name text, dept text)
  - Insert 5 records.
      1001 | Manoj | IT
      1002 | Yuvan | EEE
      1003 | Manojkumar | IT
      1004 | Ramesh | ECE
      1005 | Suresh | IT

  - Write program to get student records from database.
  - Write to student details into Excel sheet.
  - Create a table "Student_IT" and insert 3 records into it. ("IT")
  '''

import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", passwd="mysql123", database="sample")

print("Database connection established successfully")
cur=db.cursor();

query='create table student(regno int,name text,dept text)'
cur.execute(query)
query="insert into student(regno,name,dept) values(1001,'Manoj','IT')"
cur.execute(query)
query="insert into student(regno,name,dept) values(1002,'Yuvan','EEE')"
cur.execute(query)
query="insert into student(regno,name,dept) values(1003,'Manojkumar','IT')"
cur.execute(query)
query="insert into student(regno,name,dept) values(1004,'Ramesh','ECE')"
cur.execute(query)
query="insert into student(regno,name,dept) values(1005,'Suresh','IT')"
cur.execute(query)
db.commit()

query="select * from student"
cur.execute(query)
##data=cur.fetchone()
##print(data)
for data in cur.fetchall():
  print("Regno: %d, Name: %s, Dept: %s" %(data))


