# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import time

load = ' '

def WriteData(totalcars,year,monthName,day,hour,minute):

    con = sqlite3.connect('MyDB.db')
    cursor = con.cursor()
    if(totalcars<50):
        load = 'Roads are clear'
    elif(totalcars < 150):
        load = 'The roads are almost empty'
    elif(totalcars < 200):
        load = 'In places of difficulty'
    elif(totalcars < 350):
        load = 'Some difficulties'
    elif (totalcars < 450):
        load = 'Big difficulties'
    elif (totalcars < 550):
        load = 'Really bad situation'
    elif (totalcars < 650):
        load = 'You may try bysicle:)'
    elif (totalcars < 750):
        load = 'Press F'

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

