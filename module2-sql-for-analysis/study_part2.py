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

q1= '''select avg(age) from Study'''

r1 = cursor.execute(q1)
print( r1.fetchall())

q2= '''select 
count(distinct student)
from Study 
where studied = 'True'
'''

r2 = cursor.execute(q2)
print( r2.fetchall()) 

q3= '''select 
*
from STudy 
order by Student ASc;'''

r3 = cursor.execute(q3)
print( r3.fetchall()) 