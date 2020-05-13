import pandas as pd 
import os
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)
import json
from dotenv import load_dotenv 
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
import numpy as np 

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)


#df = pd.DataFrame(index, columns = ['Survived', 'Pclass', 'Name',
#                                  'Sex', 'Age', 'Siblings/Spouses Aboard',
#                                 'Parents/Children Aboard' , 'Fare'])




#engine.execute("SELECT * FROM users").fetchall()


CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
df = pd.read_csv(CSV_FILEPATH)
print(df.head())

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PW = os.getenv("DB_PW", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER,
    password=DB_PW, host=DB_HOST
    )
cursor = conn.cursor()

create_character_table = """
CREATE TABLE Titanic_Stats (
  id SERIAL PRIMARY KEY,
  Survived Int4,  
  Pclass Int4,
  Name VARCHAR(20),
  Sex VARCHAR(5),
  Age INT4,
  Siblings/Spouses Aboard Int4,
  Parents/Children Aboard Int4,
  FARE float8,
  );
"""
cursor.execute(create_character_table)
#convert df to readable in postgres
list_of_tuples = list(df.to_records(index=False))

insertion_query = f"INSERT INTO passengers (survived, pclass, name, sex, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples) # third param: data as a list of tuples!


conn.commit
cursor.close()
conn.close()





