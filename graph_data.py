#_*_coding:utf-8

import sqlite3
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

conn = sqlite3.connect("DB/test.db")
c = conn.cursor()

def graph_data():
    c.execute("SELECT time, value FROM cur WHERE time > 1455184834")
    aTime = []
    aValue = []
    for raw in c.fetchall():
        # print(datetime.datetime.fromtimestamp(raw[0]).strftime("%H:%M:%S"))
        aTime.append(datetime.datetime.fromtimestamp(raw[0]))
        aValue.append(raw[1])
    plt.plot_date(aTime, aValue, '-')
    plt.show()

graph_data()
c.close()
conn.close()