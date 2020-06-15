from datetime import datetime
import time
import sqlite3
from termcolor import colored
import sys

query = ' '
load = ' '
condition = ' '
check = 0
dayname = ' '

now = datetime.now()
dayName = (now.strftime("%A"))

def exec(year,monthName,day,hour,minute,condition,dayName):
    con = sqlite3.connect('MyDB.db')
    cursor = con.cursor()
    if(condition=='now'):
        cursor.execute("SELECT Load FROM core WHERE Year=? AND Month=? AND Day=? AND Hour=? AND Minute=?",(year,monthName,day,hour,minute))
    elif(condition=='tomorrow' or condition=='other'):
        if (dayName == 'Saturday'):
            cursor.execute("SELECT Load FROM DB_weekends WHERE Month=? AND Hour=? AND Minute=?",(monthName, hour, minute))
        else:
            cursor.execute("SELECT Load FROM DB_workdays WHERE Month=? AND Hour=? AND Minute=?",(monthName, hour, minute))
    load = str(cursor.fetchone())
    load = load.replace('(', '').replace(',', '').replace(')', '').replace('', '').replace("'",'')
    #print(year, monthName, day, hour, minute)
    if(load=='0' or load=='None'):
        print(colored('No data. please wait until database will be filled enough', 'red'))
    else:
        print(colored(str(load), 'blue'))
    con.commit()
    cursor.close()
    con.close()


def prediction(year,monthName,day,hour,minute):
    print ('Прогнозирование на какое время вы хотите знать?1-сейчас 2-завтра 3-другое время 4-выход из программы')
    query = input()
    #здесь будет принт с вариантами, например 1234 и тд
    if(query=='1'):#now
        condition = 'now'
        if(minute<=20):
            minute=0
            exec(year, monthName, day, hour, minute, condition,dayName='none')
        elif(minute<=40):
            minute = 20
            exec(year, monthName, day, hour, minute, condition, dayName='none')
        elif(minute<=60):
            minute = 40
            exec(year, monthName, day, hour, minute, condition,dayName='none')
    elif(query=='2'):#tomorrow
        condition = 'tomorrow'
        print('Это выходной день? 1-да  2-нет')
        check = input()
        if (check == '1'):
            dayName = 'Saturday'
        else:
            dayName = 'Monday'
        if (minute <= 20):
            minute = 0
            exec(year, monthName, day, hour, minute, condition,dayName)
        elif (minute <= 40):
            minute = 20
            exec(year, monthName, day, hour, minute, condition,dayName)
        elif (minute <= 60):
            minute = 40
            exec(year, monthName, day, hour, minute, condition,dayName)
    elif(query=='3'):#other
        condition = 'other'
        print('Какой месяц?(вводить на английском)')
        monthName=input()
        print('Это выходной день? 1-да  2-нет')
        check=input()
        if(check=='1'):
            dayName='Saturday'
        else:
            dayName = 'Monday'
        print('Какое время?(Часы)')
        hour=int(input())
        print('Какое время?(Минуты)')
        minute=int(input())
        if (minute <= 20):
            minute = 0
            exec(year, monthName, day, hour, minute, condition,dayName)
        elif (minute <= 40):
            minute = 20
            exec(year, monthName, day, hour, minute, condition,dayName)
        elif (minute <= 60):
            minute = 40
            exec(year, monthName, day, hour, minute, condition, dayName)
    elif (query == '4'):  # exit
        sys.exit()