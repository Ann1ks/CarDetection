# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import time

def setData(totalcars,monthName,hour,minute, load):
    con = sqlite3.connect('MyDB.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS DB_weekends(Id INTEGER PRIMARY KEY,'
                   'Month TEXT, '
                   'Hour INTEGER, '
                   'Minute INTEGER, '
                   'CarsAmount INTEGER, '
                   'Load TEXT)')

    data = [monthName, hour, minute, totalcars, load]

    cursor.execute('INSERT INTO DB_weekends(Month,Hour,Minute,CarsAmount,Load) VALUES(?,?,?,?,?) ', data)
    con.commit()
    cursor.close()
    con.close()