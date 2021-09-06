import sqlite3 as sl


#TODO create database object to abstract interaction with SQL database
con = sl.connect("kitchen_aid.db")
cur=con.cursor()

cur.execute("""CREATE TABLE inventory (
    ingredient_name varchar(255) NOT NULL PRIMARY KEY,
    ingredient_quantity smallint,
    ingredient_in_date DATE,
    is_in_stock BOOL NOT NULL DEFAULT 1
)""")

con.commit()