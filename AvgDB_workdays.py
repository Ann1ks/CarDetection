# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
import time

avg = 0
temporary = 0
def setData(totalcars,monthName,hour,minute, load):
    con = sqlite3.connect('MyDB.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS DB_workdays(Id INTEGER PRIMARY KEY,'
                   'Month TEXT, '
                   'Hour INTEGER, '
                   'Minute INTEGER, '
                   'CarsAmount INTEGER, '
                   'Load TEXT)')

    cursor.execute("SELECT CarsAmount FROM DB_workdays WHERE Month=? AND Hour=? AND Minute=?",
                   (monthName, hour, minute))
    avg = cursor.fetchone()
    temporary = avg[0]
    #avg = load.replace('(', '').replace(')', '').replace('', '')
    #avg = int(avg)
    if(temporary==0):
        temporary = totalcars
    else:
        temporary = (temporary + totalcars)/2
    cursor.execute("""UPDATE DB_workdays SET carsAmount=?, load=? WHERE Month=? AND Hour=? AND Minute=?""", (temporary, load, monthName, hour, minute))
    con.commit()
    cursor.close()
    con.close()

