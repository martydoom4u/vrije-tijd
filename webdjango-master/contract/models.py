# Django
from django.db import models

from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.utils import timezone

STATUS_CHOICES = (
    ('actief','actief'),
    ('concept', 'concept'),
    ('non-actief','non-actief'),

)



class Contract(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    organisatie = models.CharField(max_length=145, null=False, blank=False)
    tussenpersoon = models.CharField(max_length=145, null=True, blank=True)
    tussenpersoon_email = models.EmailField(null=True, blank=True)
    persoon = models.ForeignKey(User, null=False, blank=False, default=1, on_delete=models.CASCADE)
    uurtarief = models.FloatField(null=True, blank=True)
    functie = models.CharField(max_length=425, null=True, blank=True)
    begindatum = models.DateField(null=False, blank=False, default=timezone.now)
    einddatum = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='actief')

    def __str__(self):
        return str(self.persoon.email) + ' - ' + str(self.contract.organisatie) + str(self.persoon)
