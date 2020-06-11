# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import time

def setData(totalcars,year,monthName,day,hour,minute, load):
    con = sqlite3.connect('MyDB.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS core(Id INTEGER PRIMARY KEY,'
                   'Year INTEGER, '
                   'Month TEXT, '
                   'Day INTEGER, '
                   'Hour INTEGER, '
                   'Minute INTEGER, '
                   'CarsAmount INTEGER, '
                   'Load TEXT)')

    data = [year, monthName, day, hour, minute, totalcars, load]

    cursor.execute('INSERT INTO core(Year,Month,Day,Hour,Minute,CarsAmount, Load) VALUES(?,?,?,?,?,?,?) ', data)
    con.commit()
    cursor.close()
    con.close()