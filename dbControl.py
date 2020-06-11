# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import time
import AvgDB_workdays
import AvgDB_weekends
import DB_core

load = ' '

now = datetime.now()
dayName = (now.strftime("%A"))

def WriteData(totalcars,year,monthName,day,hour,minute):
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

    DB_core.setData(totalcars,year,monthName,day,hour,minute, load)
    if(dayName!="Saturday" or dayName!="Sunday"):
        AvgDB_workdays.setData(totalcars, monthName, hour, minute, load)
    else:
        AvgDB_weekends.setData(totalcars, monthName, hour, minute, load)