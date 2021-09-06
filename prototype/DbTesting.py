import sqlite3 as sl

con = sl.connect("test.db")
cur=con.cursor()

#cur.execute("""CREATE TABLE testTable (f1 TEXT,f2 INTEGER ,f3 TEXT)""")
#cur.execute("INSERT INTO testTable VALUES ('first',1,'second')")
all=cur.execute("""select * FROM testTable""").fetchall()
print(all)
con.commit()