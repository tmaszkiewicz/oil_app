import evdev
import RPi.GPIO as GPIO
import socket
from time import *
def insert_data(rfid_card):
    import pymysql
    import datetime
    import socket
    localhost = socket.gethostname()
    host = "localhost"
    srv = "jan-svr-oildb"
    user = "olejarka"
    passwd = "zAHMbwGt5NxuPTPy"
    db = "Olejarka"
    try:
        connection = pymysql.connect(host, user, passwd,db)
        connection_srv = pymysql.connect(srv, user, passwd,db)
        cursor = connection.cursor()                
        cursor_srv = connection_srv.cursor()                
    except Exception as e:            
        line = "{} // {} ERROR // {}\n".format(datetime.datetime.now(), rfid_card, e)
        with open('/var/log/czytnik.log', 'a') as f:
            f.write(line)
            f.close()
        return "BRAK POLACZENIA Z BAZA DANYCH"
    #print(localhost)
    insert = "INSERT INTO dane_wejsciowe(nr_karty, hostname) VALUES ({0},\"{1}\")".format(rfid_card,socket.gethostname())
    #print(insert)
    try:
        cursor.execute(insert)
        cursor_srv.execute(insert)
        line = "{} // Dodano poprawnie karte o numerze {}\n".format(datetime.datetime.now(), rfid_card)
    except Exception as e:
        line = "{} // {} ERROR // {}\n".format(datetime.datetime.now(), rfid_card, e)
    with open('/var/log/czytnik.log', 'a') as f:
        f.write(line)
        f.close()
    connection.commit()
    connection_srv.commit()
    connection.close()
    connection_srv.close()
    return "Dodany numer: {}".format(tag)


rfid = evdev.InputDevice('/dev/input/event0')
container = []
for event in rfid.read_loop():

    # enter into an endeless read-loop
    if event.type == evdev.ecodes.EV_KEY and event.value == 1:
        digit = evdev.ecodes.KEY[event.code]
        if len(container) == 11:
            del container[0]
            del container[0]
            del container[-1]
            #del container[-1]
            tag = "".join(i.strip('KEY_') for i in container)            
            print insert_data(tag) #Nie bedzie dzialalo w py3, zamienic na print()
            container = []
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(21, GPIO.OUT)
            GPIO.output(21,GPIO.HIGH)
            sleep(0.1)
            GPIO.output(21,GPIO.LOW)
            GPIO.cleanup()

        else:
            container.append(digit)
