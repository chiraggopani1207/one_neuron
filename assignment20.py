test1 = "This is test of emergency text system"
with open("test.txt","w")as t1:
    t1.write(test1)
    t1.close()
with open("test.txt","r")as t1:
    content=t1.read()
    print(content)
    t1.close()
"""1. Set the variable test1 to the string &#39;This is a test of the emergency text system,&#39; and save test1 to a
file named test.txt."""
"""2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1
and test 2?"""
with open("test.txt","r")as t1:
    test2=t1.read()
    print(test2)
    print(test1==test2)
    t1.close()

"""3. Create a CSV file called books.csv by using these lines:
title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992"""
data_csv1="""title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992"""
with open("books.csv","w")as csv1:
    c1=csv1.write(data_csv1)
    print(c1)

    csv1.close()
"""4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with
these fields: title (text), author (text), and year (integer)."""
import sqlite3
db =sqlite3.connect("book.db")
cursor=db.cursor()
cursor.execute("CREATE TABLE books(title text,author text, year intiger)")
db.commit()
db.close()
"""5. Read books.csv and insert its data into the book table."""
import sqlite3
import csv
conn =sqlite3.connect("book.db")
cursor=conn.cursor()
with open("book.csv","w")as file:
    books = csv.DictReader(file)
    for book in books:
        cursor.execute("INSERT INTO books values (? ? ?)",(book["title"],book["author"],book["year"]))
        conn.commit()
        conn.close()
"""6. Select and print the title column from the book table in alphabetical order."""
connector=sqlite3.connect("book.db")
cursor=connector.cursor()
output=cursor.execute("SELECT TITLE from books ORDER by title ASC")
for ele in output:
    print(ele[0])
    connector.commit()
    connector.close()
"""7. From the book table, select and print all columns in the order of publication."""
import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
output=cursor.execute(SELECT * FROM BOOKS ORDER BY year)
for record in output:
    print(record)
"""8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in
exercise 6."""
import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
print(conn)
"""9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a
Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for
test."""
import redis
conn = redis.Redis()
conn.hset('test',{
    'count':1,
    'name':'Fester Bestertester'
})
conn.hgetall('test')
"""10. Increment the count field of test and print it."""
conn.hincrby('test', 'count', 1)
conn.hget('test', 'count')
