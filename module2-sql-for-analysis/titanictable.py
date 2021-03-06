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

table_creation_sql = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
    id  SERIAL PRIMARY KEY,
    "survived" int4, -- consider boolean here
    "pclass" int4,
    "name" text,
    "sex" text,
    "age" int4,
    "sib_spouse_count" int4,
    "parent_child_count" int4,
    "fare" float8
);
"""
cursor.execute(table_creation_sql)
#convert df to readable in postgres
list_of_tuples = list(df.to_records(index=False))

insertion_query = f"INSERT INTO passengers (survived, pclass, name, sex, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples)

conn.commit() # actually save the records / run the transaction to insert rows

cursor.close()
conn.close()





