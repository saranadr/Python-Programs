


import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", passwd="mysql123", database="sample")

print("Database connection established successfully")
cur = db.cursor();

# Create a table and insert records.
#query = 'create table employee(id int, name text)'
#query = "insert into employee(id, name) values(122, 'Mohan')"
#query = "update employee set name = 'Manojkumar' where id=121"
#query = "delete from employee where id=100"
#cur.execute(query)
#db.commit()

## Fetch records from table
query="select * from employee"
cur.execute(query)
#data = cur.fetchone()
#data = cur.fetchall()
#print(data)
print("\n"+"Table Records".center(25, '*'))
for data in cur.fetchall():
  print("Id: %d, Name: %s" %(data))

print("\nProcessing completed")
