from __future__ import unicode_literals
from django.db import models
from datetime import datetime
#from organisatie.models import Organisatie
from django.contrib.auth.models import User
from contract.models import Contract
from weekstaat.models import Weekstaat

class Factuur(models.Model):
    id = models.AutoField(primary_key=True)
    factuurdatum = models.DateField(null=False, blank=False)
    vervaldatum = models.DateField(null=False, blank=False, default=datetime.now())
    werknemer = models.ForeignKey(User, null=False, blank=False,on_delete=models.CASCADE)
    #organisatie_werknemer = models.ForeignKey(Organisatie, null=False, blank=False)
    #contractregel = models.ForeignKey(Contractregel, null=False, blank=False,on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, null=False, blank=False,on_delete=models.CASCADE)
    weekstaat = models.ManyToManyField(Weekstaat)
    totaal_excl_btw = models.FloatField(null=False, blank=False)
    totaal_incl_btw = models.FloatField(null=False, blank=False)
    btw_procent = models.CharField(null=False, blank=False, max_length=10)
    btw_bedrag = models.FloatField(null=False, blank=False)

    def __str__(self):
        return str(self.werknemer.email) + ' - ' + str(self.contract)
