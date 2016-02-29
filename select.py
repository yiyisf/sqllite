#_*_coding:utf-8
import sqlite3

conn = sqlite3.connect("DB/test.db")
c = conn.cursor()

def read_from_db():
    c.execute("SELECT * FROM cur")
    for row in c.fetchall():
        print(row)

read_from_db()
c.close()
conn.close()
