from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class Jaar(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    jaar = models.CharField(null=False, blank=False, default=str(datetime.now().year), max_length=4)

    def __str__(self):
        return str(self.jaar)


class Week(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)

    def __str__(self):
        return str(self.id)





class Weekstaat(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    #status = models.ForeignKey(Status, null=False, blank=False, default=1,on_delete=models.CASCADE)
    jaar = models.ForeignKey(Jaar, default=datetime.now().year, null=False, blank=False,on_delete=models.CASCADE)
    week = models.ForeignKey(Week, default=date.today().isocalendar()[1], null=False, blank=False,on_delete=models.CASCADE)
    werknemer = models.ForeignKey(User, related_name='weekstaat_werknemer', null=False, blank=False, default=1,on_delete=models.CASCADE)
    maandag = models.FloatField(null=True, blank=True)
    dinsdag = models.FloatField(null=True, blank=True)
    woensdag = models.FloatField(null=True, blank=True)
    donderdag = models.FloatField(null=True, blank=True)
    vrijdag = models.FloatField(null=True, blank=True)
    zaterdag = models.FloatField(null=True, blank=True)
    zondag = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.jaar) + ' week ' + str(self.week) + str(self.werknemer)
