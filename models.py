from django.db import models
#from django import forms
#from django.contrib.admin import widgets
#from datetime import datetime
#from django.utils.timezone import now

class employee(models.Model):
    TimeCardNr = models.CharField(max_length=50,blank=True,null=True)
    PersonalNr = models.CharField(max_length=50,blank=True,null=True)
    Name = models.CharField(max_length=50,blank=True,null=True)
    WorkCenterId = models.CharField(max_length=50,blank=True,null=True)
    LoginTime = models.DateTimeField(blank=True,null=True)
    LogoutTime = models.DateTimeField(blank=True,null=True)
    class Meta:
        verbose_name_plural = 'employee s'


    def  __str__(self):
        return str(self.Name + " " + self.TimeCardNr)

                                                # Create your models here.
class odczyt(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    nr_karty = models.CharField(max_length=6,blank=True,null=True)
    hostname = models.CharField(max_length=12,blank=True,null=True)
    timestamp = models.DateTimeField(blank=True,null=True)
    class Meta:
        verbose_name_plural = 'odczyt y'

    def  __str__(self):
        return  str(self.nr_karty) # + " " + self.timestamp + " " )
