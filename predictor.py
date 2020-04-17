from datetime import datetime
import time
import sqlite3

carsAmount = 0
query = ' '
now = datetime.today()
year = int(now.strftime("%Y"))
month = int(now.strftime("%m"))
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))
seconds = int(now.strftime("%S"))
monthname = ' '

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

def exec():
    con = sqlite3.connect('MyDB.db')
    cursor = con.cursor()
    cursor.execute('SELECT CarsAmount FROM core WHERE Day=14 AND Hour=22 AND Minute=3')
    carsAmount = str(cursor.fetchone())
    carsAmount = int(carsAmount.replace('(', '').replace(',', '').replace(')', ''))
    print(carsAmount)
    if(carsAmount<120):
        pass
    if(carsAmount<200):
        pass



    con.commit()
    cursor.close()
    con.close()


def prediction():
    print ('Прогнозирование на какое время вы хотите знать?')
    query = input()
    if(query=='сейчас'):
        if(minute%20!=0):
            if(minute<60):
                 exec()
            if(minute<40):
                pass
            if(minute<60):
                pass
        else:
            pass
    elif():
        pass


'''
я буду получать на какое время пользователь хочет получить прогноз, нужен алгоритм примерных точек соприкосновения(только будущих) минуты отдельно считать, а вот уже часы там заебись
буду вытягивать из бд число машин на нужное время и буду сравнивать это число с какими-то уже заданными значениями нагрузки траффика
 '''