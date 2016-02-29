# coding:utf-8
import random
import sqlite3
import datetime
import time

conn = sqlite3.connect("DB/test.db")
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS cur (Dttime TEXT , time REAL , cur TEXT,value REAL )')


def dynamic_insert():
    Vtime = time.time()
    dt = str(datetime.datetime.fromtimestamp(Vtime).strftime('%Y-%m-%d %H:%M:%S'))
    cur = 'AUD'
    value = random.randrange(10,100)
    c.execute("INSERT INTO cur (Dttime, time, cur, value) VALUES (?, ?, ?, ?)",
              (dt, Vtime, cur, value))
    conn.commit()


create_table()
for i in range(10):
    dynamic_insert()
    time.sleep(1)

c.close()
conn.close()


