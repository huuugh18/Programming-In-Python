## [FCC full course sqlite db with python]('https://www.youtube.com/watch?v=byHcYRpMgI4')
import sqlite3

# connect to db
conn = sqlite3.connect('customer.db')

# create cursor to interact with db
c = conn.cursor()

# create a table - triple quotes allow you to use multiple lines for the command
c.execute('''CREATE TABLE IF NOT EXISTS customers (
      first_name TEXT,
      last_name TEXT,
      email TEXT
   )''')

#DATATYPES:  NULL | INTEGER | REAL (decimal) | TEXT | BLOB (image, mp3, etc)

#  --------- CREATE A CUSTOMER ---------
# c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@something.com')")

# --------- INSERT MANY CUSTOMERS ---------
many_customers = [
   ('wes', 'brown', 'wes@brown.com'),
   ('dude', 'duders', 'dude@dudes.com'),
   ('some', 'guy', 'some@guy.com')
]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)



# --------- PRIMARY KEY ---------
c.execute("SELECT rowid, * FROM customers") # => (1, 'John', 'Elder', 'john@something.com')
# print(c.fetchone())

# --------- WHERE CLAUSE ---------
# can use >=, <=, = logical operaters
# LIKE searches text - WHERE last_name LIKE 'Br%'  || WHERE email LIKE '%codemy.com'

# c.execute("SELECT * FROM customers WHERE last_name = 'Elder'")
# print(c.fetchone())

# --------- UPDATE RECORDS ---------
# c.execute("""UPDATE customers SET first_name = 'Bob'
#    WHERE last_name = 'Elder'
# """)

# use row record instead to avoid changing multiple 'Elders' etc.
# c.execute("""UPDATE customers SET first_name = 'Bob'
#    WHERE rowid = 1
# """)

# --------- DELETE RECORDS ---------
# c.execute("DELETE from customers WHERE rowid = 4")


# --------- ORDERING RECORDS ---------
c.execute("SELECT rowid, * FROM customers ORDER BY last_name ASC")

# --------- AND/OR ---------
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'br%' AND rowid = 3")

c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'br%' OR rowid = 3")

# --------- LIMITING RESULTS ---------
c.execute("SELECT rowid, * FROM customers LIMIT 2")

# --------- DROP A TABLE ---------------
# c.execute("DROP TABLE customers")


# -------- GROUP BY METHOD -----------
# https://www.youtube.com/watch?v=iXYeb2artTE&t=556s
# can use to get groups of data
# example of methods of coffee brewing in the video
# SELECT method, AVG(rating) FROM beans GROUP BY method;
   # returns table with methods and their average rating


# --------- QUERY DATABASE ---------
# c.execute("SELECT * FROM CUSTOMERS")
# c.fetchone()
# print(c.fetchmany(3)[1][1])
items = c.fetchall()

for item in items:
   print(item)

c.ex
#save changes to the db
conn.commit()

#close connection
conn.close()

