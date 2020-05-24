# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import time
import AvgDB_workdays
import AvgDB_weekends

now = datetime.today()
monthC = int(now.strftime("%m"))
hourC = int(now.strftime("%H"))
minuteC = int(now.strftime("%M"))
secondsC = int(now.strftime("%S"))
monthNameC = ' '
counter = 0

hourC = 0
minuteC = 0
monthC = 1
def setMonthName(monthNameC):
    if monthC == 1:
        monthNameC = "January"
    if monthC == 2:
        monthNameC = "February"
    if monthC == 3:
        monthNameC = "March"
    if monthC == 4:
        monthNameC = "April"
    if monthC == 5:
        monthNameC = "May"
    if monthC == 6:
        monthNameC = "June"
    if monthC == 7:
        monthNameC = "July"
    if monthC == 8:
        monthNameC = "August"
    if monthC == 9:
        monthNameC = "September"
    if monthC == 10:
        monthNameC = "October"
    if monthC == 11:
        monthNameC = "November"
    if monthC == 12:
        monthNameC = "December"
    return monthNameC


monthNameC = setMonthName(monthNameC)

while counter<864:#amount of rows
    con = sqlite3.connect('MyDB.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS DB_workdays(Id INTEGER PRIMARY KEY,'
                   'Month TEXT, '
                   'Hour INTEGER, '
                   'Minute INTEGER, '
                   'CarsAmount INTEGER, '
                   'Load TEXT)')
    data = [monthNameC, hourC, minuteC, 0, 0]
    cursor.execute('INSERT INTO DB_workdays(Month,Hour,Minute,CarsAmount,Load) VALUES(?,?,?,?,?) ', data)
    con.commit()
    cursor.close()
    con.close()
    minuteC+=20
    if(minuteC>=60):
        minuteC=0
        hourC+=1
    if(hourC==24):
        hourC = 0
        minuteC = 0
        monthC+=1
        monthNameC = setMonthName(monthNameC)
    counter+=1