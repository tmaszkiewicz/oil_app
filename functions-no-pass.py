#import csv
import time,datetime
#from .models import foamFile,foamRow,message,lastRefresh ----->!!!!!message
#import pytz
#from os import listdir
#from os.path import isfile, join
#from django.db.models import Q
from os import getenv
from django.utils import timezone
from .models import employee,odczyt
#import sqlalchemy
#from sqlalchemy.dialects.mssql import pymssql
import pymssql
import pymysql
import pymysql.cursors

def readEmployees():
    #timestamp = time.time()
    #tzone = pytz.timezone('Europe/Warsaw')

    effDate = timezone.now() + timezone.timedelta(days=-10)
    sql = "SELECT * FROM EMPLOYEE WHERE WORKCENTERID LIKE 'TA-TAP%'" # WHERE LoginTime >" + str(effDate) #  and LoginTime> '"+str(lastRefresh.objects.last().lastRefresh)+"'" #'2018-10-16 14:13:34'"
    #sql = "SELECT * FROM EMPLOYEE" # WHERE LoginTime >" + str(effDate) #  and LoginTime> '"+str(lastRefresh.objects.last().lastRefresh)+"'" #'2018-10-16 14:13:34'"
    #sql = "SELECT * FROM EMPLOYEE WHERE TimeClient >" +"'"+str(effDate)+"' and TimeClient> '"+str(lastRefresh.objects.last().lastRefresh)+"'" #'2018-10-16 14:13:34'"
    #sql = "SELECT * FROM MESSAGE WHERE TimeClient >" +"'"+str(effDate)+"' and TimeClient> '"+str(lastRefresh.objects.last().lastRefresh)+ "' and WorkCenterId = '"+WorkCenter+"'"
    #sql = "SELECT * FROM MESSAGE WHERE TimeClient >" +"'"+str(effDate)+"'"
    conn = pymssql.connect('192.168.41.24\SQLEXPRESS','spot_sql','password', 'SFC-Polipol')
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    #for each in rows:
    #    print("ID=%d, Name=%s" % (each[0], each[1]))
    employee.objects.all().delete()# ----> usuwanie starych userow wyfiltruj userow z logowaniem >= data

        
    for each in rows:
        employ = employee()
        TimeCardNr = employee.objects.filter(TimeCardNr=each[0]).first() #=each[0] --> MessqgeId
        if TimeCardNr==None:
            employ.TimeCardNr = each[0]  #'Nr Karty
            employ.PersonalNr = each[1]  #'Nr osobowy
            employ.Name = each[2]  #'Imie Nazwisko
            employ.WorkCenterId = each[6]  #'Imie Nazwisko
            employ.LoginTime = each[7]  #
            employ.LogoutTime = each[8]  #
            try:
                employ.save()
            except Exception as e:
                print("Blad -  nie dodanaa - {0}".format(e))
            #lastRefr = lastRefresh()
            #lastRefr.lastRefresh =  timezone.now()
            #lastRefr.save()
    #Dodac usuwanie nadmiarowych uzytkownikow

    #sql2 zczytywanie danych z olejarek
    return True

def readEmployees_cho():
    #timestamp = time.time()
    #tzone = pytz.timezone('Europe/Warsaw')

    effDate = timezone.now() + timezone.timedelta(days=-10)
    sql = "SELECT * FROM EMPLOYEE WHERE WORKCENTERID LIKE 'TA-TA%'" # WHERE LoginTime >" + str(effDate) #  and LoginTime> '"+str(lastRefresh.objects.last().lastRefresh)+"'" #'2018-10-16 14:13:34'"
    #sql = "SELECT * FROM EMPLOYEE" # WHERE LoginTime >" + str(effDate) #  and LoginTime> '"+str(lastRefresh.objects.last().lastRefresh)+"'" #'2018-10-16 14:13:34'"
    #sql = "SELECT * FROM EMPLOYEE WHERE TimeClient >" +"'"+str(effDate)+"' and TimeClient> '"+str(lastRefresh.objects.last().lastRefresh)+"'" #'2018-10-16 14:13:34'"
    #sql = "SELECT * FROM MESSAGE WHERE TimeClient >" +"'"+str(effDate)+"' and TimeClient> '"+str(lastRefresh.objects.last().lastRefresh)+ "' and WorkCenterId = '"+WorkCenter+"'"
    #sql = "SELECT * FROM MESSAGE WHERE TimeClient >" +"'"+str(effDate)+"'"
    conn = pymssql.connect('192.168.25.70\SQLEXPRESS','sa','Membrain123', 'SFC-Polipol')
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    #for each in rows:
    #    print("ID=%d, Name=%s" % (each[0], each[1]))
    employee.objects.all().delete()# ----> usuwanie starych userow wyfiltruj userow z logowaniem >= data

        
    for each in rows:
        employ = employee()
        TimeCardNr = employee.objects.filter(TimeCardNr=each[0]).first() #=each[0] --> MessqgeId
        if TimeCardNr==None:
            employ.TimeCardNr = each[0]  #'Nr Karty
            employ.PersonalNr = each[1]  #'Nr osobowy
            employ.Name = each[2]  #'Imie Nazwisko
            employ.WorkCenterId = each[6]  #'Imie Nazwisko
            employ.LoginTime = each[7]  #
            employ.LogoutTime = each[8]  #
            try:
                employ.save()
            except Exception as e:
                print("Blad -  nie dodanaa - {0}".format(e))
            #lastRefr = lastRefresh()
            #lastRefr.lastRefresh =  timezone.now()
            #lastRefr.save()
    #Dodac usuwanie nadmiarowych uzytkownikow

    #sql2 zczytywanie danych z olejarek
    return True
def readOdczyt():
    sql_odczyty = "SELECT * FROM dane_wejsciowe" # WHERE LoginTime >" + str(effDate) #  and LoginTime> '"+str(lastRefresh.objects.last().lastRefresh)+"'" #'2018-10-16 14:13:34'"

    conn_odczyty = pymysql.connect(host='192.168.41.205',user='olejarka',password='zAHMbwGt5NxuPTPy', db='Olejarka', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)   
    cursor_odczyt = conn_odczyty.cursor()
    cursor_odczyt.execute(sql_odczyty)
    rows_odczyt=cursor_odczyt.fetchall()
    conn_odczyty.close()
    for each in rows_odczyt:
        odcz=odczyt()
        print(each['timestamp'])
        znaleziono = odczyt.objects.filter(nr_karty=each['nr_karty'],timestamp=each['timestamp']).first()
        if znaleziono==None:
            odcz.nr_karty=each['nr_karty']
            odcz.timestamp=each['timestamp']
            odcz.hostname=each['hostname']
            try:
                odcz.save()
            except Exception as e:
                print("Blad - nie dodana - {0}".format(e))
    return True

def readOdczyt_cho():
    sql_odczyty = "SELECT * FROM dane_wejsciowe_cho" # WHERE LoginTime >" + str(effDate) #  and LoginTime> '"+str(lastRefresh.objects.last().lastRefresh)+"'" #'2018-10-16 14:13:34'"

    conn_odczyty = pymysql.connect(host='192.168.41.205',user='olejarka',password='zAHMbwGt5NxuPTPy', db='Olejarka', charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)   
    cursor_odczyt = conn_odczyty.cursor()
    cursor_odczyt.execute(sql_odczyty)
    rows_odczyt=cursor_odczyt.fetchall()
    conn_odczyty.close()
    for each in rows_odczyt:
        odcz=odczyt()
        print(each['timestamp'])
        znaleziono = odczyt.objects.filter(nr_karty=each['nr_karty'],timestamp=each['timestamp']).first()
        if znaleziono==None:
            odcz.nr_karty=each['nr_karty']
            odcz.timestamp=each['timestamp']
            odcz.hostname=each['hostname']
            try:
                odcz.save()
            except Exception as e:
                print("Blad - nie dodana - {0}".format(e))
    return True


def read_all():
    readEmployees() #-> docelowo do wlaczenia 25.10.2019
    readOdczyt()
    return True

def read_all_cho():
    readEmployees_cho() #-> docelowo do wlaczenia 25.10.2019
    readOdczyt_cho()
    return True
