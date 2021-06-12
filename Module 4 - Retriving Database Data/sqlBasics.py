import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# conn = sqlite3.connect('dataProgramming2.db')

# c = conn.cursor()

# c.execute('''CREATE TABLE IF NOT EXISTS users(
#    FirstName VARCHAR(30) NOT NULL,
#    LastName VARCHAR(30) NOT NULL,
#    USERID INT NOT NULL UNIQUE,
#    PRIMARY KEY (USERID)
# )''')

def print_results(results):
   results = results.fetchall()
   for res in results:
      print(res)

def addUser(first_name, last_name, id):
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()
   c.execute("INSERT INTO users VALUES(?,?,?)", (first_name, last_name, id))
   conn.commit()
   conn.close()

# addUser('Blue', 'Cup', 1)
# addUser('Orange', 'Cup', 2)
# addUser('Black', 'Plate', 3)
# addUser('Black', 'Bowl', 4)

def getAllUsers():
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()
   users = c.execute("SELECT * FROM users")
   print_results(users)
   conn.commit()
   conn.close()

# getAllUsers()

def getFirstNames():
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()
   names = c.execute("SELECT FirstName FROM users")
   print_results(names)
   conn.commit()
   conn.close()

# getFirstNames()

def getUserById(id):
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()
   user = c.execute("SELECT * FROM users WHERE USERID = (?)", (id, ))
   print_results(user)
   conn.commit()
   conn.close()

# getUserById(3)

#-----  GET LIST OF COLUMNS OF A TABLE ------
def getTableColumnLists():
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()
   # results = c.execute("SELECT * FROM (?)", (table_name, ))
   results = c.execute("SELECT * FROM users")
   results = results.fetchall()
   # print(results)
   df = pd.DataFrame.from_records(results)
   print(df)


   conn.commit()
   conn.close()

# getTableColumnLists()

def getEvenIdUsers():
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()

   results = c.execute('SELECT USERID, FirstName FROM users WHERE USERID %2 = 0')
   print_results(results)

   conn.commit()
   conn.close()

# getEvenIdUsers()

def getAliasFirstName():
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()

   results = c.execute('SELECT FirstName AS Name, USERID as id FROM users')
   print_results(results)

   conn.commit()
   conn.close()

# getAliasFirstName()

def getLimitedUsers(amount):
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()

   results = c.execute('SELECT * FROM users LIMIT (?)', (amount, ))
   print_results(results)

   conn.commit()
   conn.close()

# getLimitedUsers(3)

def getOrderedUsers():
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()

   results = c.execute('SELECT * FROM users ORDER BY LastName ASC')
   print_results(results)

   conn.commit()
   conn.close()

# getOrderedUsers()

def getMinMax():
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()

   results = c.execute('SELECT min(USERID), max(USERID) FROM users')
   print_results(results)

   conn.commit()
   conn.close()

# getMinMax()

def useInQuery():
   conn = sqlite3.connect('dataProgramming2.db')
   c = conn.cursor()

   # use to determine whether value matches any value in a list or subquery
   # 'SELECT * FROM users WHERE FirstName IN (SELECT FirstName FROM users WHERE LastName = "Plate"')
   # results = c.execute('SELECT * FROM users WHERE FirstName IN (SELECT FirstName FROM users WHERE LastName = "Plate"))')
   results = c.execute('SELECT * FROM users WHERE FirstName IN ("Black", "Orange")')
   print_results(results)

   conn.commit()
   conn.close()

# useInQuery()



# conn.commit()

# conn.close()