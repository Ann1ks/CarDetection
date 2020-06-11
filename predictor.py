from datetime import datetime
import time
import sqlite3

query = ' '
load = ' '
condition = ' '

def exec(year,monthName,day,hour,minute,condition):
    con = sqlite3.connect('MyDB.db')
    cursor = con.cursor()
    cursor.execute("SELECT Load FROM core WHERE Year=? AND Month=? AND Day=? AND Hour=? AND Minute=?", (year,monthName,day,hour,minute))
    load = str(cursor.fetchone())
    load = load.replace('(', '').replace(',', '').replace(')', '').replace('', '')
    print(year, monthName, day, hour, minute)
    print(load)
    con.commit()
    cursor.close()
    con.close()


def prediction(year,monthName,day,hour,minute):
    print ('Прогнозирование на какое время вы хотите знать?')
    query = input()
    #здесь будет принт с вариантами, например 1234 и тд
    if(query=='1'):#now
        condition = 'now'
        if(minute<=20):
            minute=0
            exec(year,monthName,day,hour,minute)
        elif(minute<=40):
            minute = 20
            exec(year,monthName,day,hour,minute)
        elif(minute<=60):
            minute = 40
            exec(year,monthName,day,hour,minute)
    elif(query=='2'):#tomorrow
        condition = 'tomorrow'
        pass
    elif(query=='3'):#other
        condition = 'other'
        pass



