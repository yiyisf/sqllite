# _*_ coding:utf-8

import sqlite3

conn = sqlite3.connect("DB/test.db", timeout=5)
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS test (account REAL, cif REAL , id TEXT,name TEXT)')


def entry_rec():
    c.execute("INSERT INTO test VALUES (01287565000014,100000001,'a0001','sandra')")
    conn.commit()
    c.close()

create_table()
entry_rec()
conn.close()
