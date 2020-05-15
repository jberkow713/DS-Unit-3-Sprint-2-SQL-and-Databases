import sqlite3
import pandas as pd 
import os
import json
from dotenv import load_dotenv 
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
import numpy as np 


connection = sqlite3.connect("demo_data1.sqlite3")
cursor = connection.cursor()

table_creation_sql = """
CREATE TABLE IF NOT EXISTS Demo (
    id  SERIAL PRIMARY KEY,
    "s" string, 
    "x" int,
    "y" int
);
"""
cursor.execute(table_creation_sql)
connection.commit()

q2 = """INSERT INTO Demo ("s", "x", "y")
VALUES ('g', '3', '9');"""

cursor.execute(q2)
connection.commit()

q3 = """INSERT INTO Demo ("s", "x", "y")
VALUES ('v', '5', '7');"""

cursor.execute(q3)
connection.commit()

q4 = """ INSERT INTO Demo ("s", "x", "y")
VALUES ('f', '8', '7');"""

cursor.execute(q4)
connection.commit()


connection.commit()


#results = cursor.fetchall()
#for row in results:
#    print(type(row), row)

# actually save the records / run the transaction to insert rows




cursor.close()
connection.close()