import sqlite3
import pandas as pd


def open_db():
   conn = sqlite3.connect('exercise2.db')
   c = conn.cursor()
   return (c,conn)

def close_db(c):
   c.commit()
   c.close()

def build_assessments_table():
   c, conn = open_db()

   c.execute('''CREATE TABLE IF NOT EXISTS assessments(
      code_module TEXT,
      code_presentation TEXT,
      id_assessment INTEGER,
      assessment_type TEXT,
      date INT,
      weight INT)
    ''')
   close_db(conn)

# build_assessments_table()

import os
import csv

def execute_command(command):
   conn = sqlite3.connect('exercise2.db')
   c = conn.cursor()
   c.execute(command)
   conn.commit()
   conn.close()


def clear_assessment_data():
   command = 'DELETE FROM assessments'
   execute_command(command)

# clear_assessment_data()


def set_assessment_data():
   with open('data/courses.csv', 'rt') as fin:
      reader = csv.reader(fin)
      print(reader)
      # #skip header row
      # next(reader)
      # to_db = [(row[0], row[1], row[2], row[3], row[4], row[5])]

      # headers = "code_module","code_presentation","id_assessment","assessment_type","date","weight"
      # command = 'INSERT INTO assessments VALUES (?,?,?,?,?,?);', to_db

      # c,conn = open_db()

      # c.executemany(command)
      # close_db(conn)
      # # cur.executemany('INSERT INTO courses(code_module, code_presentation, module_presentation_length) VALUES (?, ?, ?);', to_db)   ')

set_assessment_data()