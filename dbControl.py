# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import time

now = datetime.now()
year = int(now.strftime("%Y"))
month = int(now.strftime("%m"))
monthname = ' '
day = int(now.strftime("%d"))
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))

if month==1:
    monthname = "January"
if month==2:
    monthname = "February"
if month==3:
    monthname = "March"
if month==4:
    monthname = "April"
if month==5:
    monthname = "May"
if month==6:
    monthname = "June"
if month==7:
    monthname = "July"
if month==8:
    monthname = "August"
if month==9:
    monthname = "September"
if month==10:
    monthname = "October"
if month==11:
    monthname = "November"
if month==12:
    monthname = "December"


def WriteData(totalcars):
    con = sqlite3.connect('MyDB.db')
    cursor = con.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS core(Id INTEGER PRIMARY KEY,'
                   'Year INTEGER, '
                   'Month TEXT, '
                   'Day INTEGER, '
                   'Hour INTEGER, '
                   'Minute INTEGER, '
                   'CarsAmount INTEGER)')

    data = [year, monthname, day, hour, minute, totalcars ]

    cursor.execute('INSERT INTO core(Year,Month,Day,Hour,Minute,CarsAmount) VALUES(?,?,?,?,?,?) ', data)
    con.commit()
    cursor.close()
    con.close()

