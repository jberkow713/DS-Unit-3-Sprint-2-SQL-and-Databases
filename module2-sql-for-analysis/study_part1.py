import sqlite3
import pandas as pd 
import os
import json
from dotenv import load_dotenv 
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
import numpy as np 


connection = sqlite3.connect("study_part1.sqlite3")
cursor = connection.cursor()


table_creation_sql = """
CREATE TABLE IF NOT EXISTS Study (
    id  SERIAL PRIMARY KEY,
    "student" string, 
    "studied" string,
    "grade" int,
    "age" int,
    "sex" string
);
"""
cursor.execute(table_creation_sql)
connection.commit()

q2 = """INSERT INTO Study ("student", "studied", "grade", "age", "sex")
VALUES ('Lion-O', 'True', '85', '24', 'male');"""

cursor.execute(q2)
connection.commit()

q3 = """INSERT INTO Study ("student", "studied", "grade", "age", "sex")
VALUES ('Cheetara', 'True', '95', '22', 'Female');"""

cursor.execute(q3)
connection.commit()

q4 = """ INSERT INTO Study ("student", "studied", "grade", "age", "sex")
VALUES ('Mumm-Ra', 'False', '65', '153', 'Male');"""

cursor.execute(q4)
connection.commit()

q5 = """INSERT INTO Study ("student", "studied", "grade", "age", "sex")
VALUES ('Snarf', 'False', '70', '15', 'Male');"""

cursor.execute(q5)
connection.commit()

q6 = """INSERT INTO Study ("student", "studied", "grade", "age", "sex")
VALUES ('Panthro', 'True', '80', '30', 'Male');"""

cursor.execute(q6)
connection.commit()


#results = cursor.fetchall()
#for row in results:
#    print(type(row), row)

# actually save the records / run the transaction to insert rows




cursor.close()
connection.close()



#connection = sqlite3.connect(DATABASE_FILEPATH)
#cursor = connection.cursor()
#r1 = curs.execute(q1)
#r2 = curs.execute(q2)
#r3 = curs.execute(q3)
#r4 = curs.execute(q4)
#r5 = curs.execute(q5)
#r6 = curs.execute(q6)

#curs.execute(q1).fetchall()
#curs.execute(q1).fetchall()
#curs.execute(q1).fetchall()
#curs.execute(q1).fetchall()
#curs.execute(q1).fetchall()
#curs.execute(q1).fetchall()