import sqlite3

## connect to sqlite
connection = sqlite3.connect("student.db")

## Create a curor object to insert record, create table, retrieve
cursor = connection.cursor()

## create the table
table_info = """
Create table STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);

"""

cursor.execute(table_info)

## Inert some more records
cursor.execute('''Insert Into STUDENT values('Mad', 'Data Science','A', '90')''')
cursor.execute('''Insert Into STUDENT values('Deven', 'Data Engineer', 'A','40')''')
cursor.execute('''Insert Into STUDENT values('Chris', 'Data Analyst', 'A','85')''')
cursor.execute('''Insert Into STUDENT values('Saurav', 'Data Science', 'A','95')''')
cursor.execute('''Insert Into STUDENT values('Arjun', 'Web dev', 'A','75')''')
cursor.execute('''Insert Into STUDENT values('Omkar', 'DSA', 'A','65')''')

# Display all the records
print("The inserted records are: ")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()
