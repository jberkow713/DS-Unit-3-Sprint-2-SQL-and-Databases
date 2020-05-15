import sqlite3
import pandas as pd 
import os
import json
from dotenv import load_dotenv 
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
import numpy as np 


connection = sqlite3.connect("northwind_small.sqlite3")
cursor = connection.cursor()

q1 = '''select productname, unitprice
from Product
group by ProductName
order by unitprice DESC
limit 10 ;'''

r1 = cursor.execute(q1)

print( r1.fetchall())

q2 = '''select FirstName, avg(HireDate - BirthDate) as avg_years
from Employee
group by FirstName;'''

r2 = cursor.execute(q2)

print( r2.fetchall())

q3 = '''select productname, unitprice, SupplierName
from ProductDetails_V
group by SupplierName
order by unitprice DESC
limit 10 ;'''

r3 = cursor.execute(q3)

print( r3.fetchall())

q5 = '''select
p.productname, p.unitprice, s.companyname
from Product as p, Supplier as s 
where p.SupplierId = s.Id 
group by s.CompanyName
order by p.UnitPrice DESC 
limit 10;'''

r5 = cursor.execute(q5)

print( r5.fetchall())

q4= '''select categoryid,
COUNT(distinct productname) as category_count
FROM product
GROUP by categoryid
order by category_count DESC;'''

r4 = cursor.execute(q4)
print( r4.fetchall())

q6= '''select 
p.productname, c.categoryname,
count(distinct p.productname) as category_count
from product as p, category as c 
where c.id = p.categoryid 
group by c.categoryname
order by category_count DESC;'''

r6 = cursor.execute(q6)
print( r6.fetchall())