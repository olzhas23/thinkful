__author__ = 'Olzhas'
import psycopg2
import sys


cars= (
    (1, 'Audi', 34536),
    (2, 'BMW', 34933),
    (3, 'GMC', 2343),
    (4, "Mercedes", 34566)
)
con=None

try:



    con = psycopg2.connect(database="testdb")
    cur=con.cursor()
    cur.execute('DROP table IF EXISTS Cars')
    cur.execute('CREATE TABLE cars(ID INT primary key, name text, price integer )')
    query= "insert into cars (ID, NAME , Price)values (%s,%s,%s)"
    cur.executemany(query,cars)
    con.commit()
except psycopg2.DatabaseError,e:
    print "Error %s" %e


finally:
  if con:
    con.close()


