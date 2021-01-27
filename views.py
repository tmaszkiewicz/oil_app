from django.shortcuts import render
from django.http import HttpResponse
from .functions import read_all,read_all_cho
from .models import *
import time,datetime
from django.utils import timezone
def report(request, * argc, **argv):
    url='oil_app/report.html'
    context = {
    }
    
    read_all()

    effDate = timezone.now() + timezone.timedelta(days=-2)
    odczyty=odczyt.objects.all().order_by('-timestamp')
    for o in odczyty:
        try:
            karta="00{0}".format(o.nr_karty)
    
            employ = employee.objects.get(TimeCardNr=karta)
            o.name=employ.Name
            o.save()
        except:
            None
            #print("Nie znaleziono pracownika {}".format(karta))

    context['odczyty'] = odczyty
    
    return render(request,url,context)

def report_all_users(request, *argc, **argv):
    url='oil_app/report_all_users.html'
    context = {

    }
    wiersz = {

    }

    effDate = timezone.now() + timezone.timedelta(days=-3)
    wiersze=[]
    read_all()
    employees=employee.objects.all()
    for e in employees:
        wiersz ={}
        wiersz['TimeCardNr']=e.TimeCardNr
        wiersz['PersonalNr']=e.PersonalNr
        wiersz['Name']=e.Name
        wiersz['WorkCenterId']=e.WorkCenterId
        wiersz['LoginTime']=e.LoginTime 
        wiersz['LogoutTime']=e.LogoutTime 
        wiersz['ilosc_odczytow']=odczyt.objects.filter(nr_karty=e.TimeCardNr[2:]).count()
        wiersz['ilosc_odczytow_48']=odczyt.objects.filter(nr_karty=e.TimeCardNr[2:], timestamp__gt=effDate).count()
        try:
            wiersz['ostatni_odczyt']=odczyt.objects.filter(nr_karty=e.TimeCardNr[2:]).last().timestamp
        except:
            wiersz['ostatni_odczyt']=""
        #20-05-2020
        #wiersz['hostname']=odczyt.objects.filter(ar_karty=e.TimeCardNr[2:], timestamp__gt=effDate).first.hostname
        wiersze.append(wiersz)

    context['wiersze']=sorted(wiersze, key = lambda k: k['ilosc_odczytow'], reverse=True)
    return render(request,url,context)


def report_all_users_cho(request, *argc, **argv):
    url='oil_app/report_all_users_cho.html'
    context = {

    }
    wiersz = {

    }

    effDate = timezone.now() + timezone.timedelta(days=-3)
    wiersze=[]
    wiersze_s=[]
    read_all_cho()
    employees=employee.objects.all()
    for e in employees:
        wiersz ={}
        wiersz['TimeCardNr']=e.TimeCardNr
        wiersz['PersonalNr']=e.PersonalNr
        wiersz['Name']=e.Name
        wiersz['WorkCenterId']=e.WorkCenterId
        wiersz['LoginTime']=e.LoginTime 
        wiersz['LogoutTime']=e.LogoutTime 
        wiersz['ilosc_odczytow']=odczyt.objects.filter(nr_karty=e.TimeCardNr[2:]).count()
        wiersz['ilosc_odczytow_48']=odczyt.objects.filter(nr_karty=e.TimeCardNr[2:], timestamp__gt=effDate).count()
        try:
            wiersz['ostatni_odczyt']=odczyt.objects.filter(nr_karty=e.TimeCardNr[2:]).last().timestamp
        except:
            wiersz['ostatni_odczyt']=timezone.now()-datetime.timedelta(days=365)
        #20-05-2020
        #wiersz['hostname']=odczyt.objects.filter(ar_karty=e.TimeCardNr[2:], timestamp__gt=effDate).first.hostname
        wiersze.append(wiersz)
    wiersze_s= sorted(wiersze, key = lambda k: k['ostatni_odczyt'], reverse=True)
    for i in wiersze_s:
        if(i['ostatni_odczyt']<=timezone.now()-datetime.timedelta(days=365)):
            i['ostatni_odczyt']=""
    #context['wiersze']=sorted(wiersze, key = lambda k: k['ostatni_odczyt'], reverse=True)
    context['wiersze']=wiersze_s
    #context['wiersze']=sorted(wiersze, key = lambda k: k['ostatni_odczyt'], reverse=True)
    print ("----{0}----".format(effDate))
    return render(request,url,context)

# Create your views here.
