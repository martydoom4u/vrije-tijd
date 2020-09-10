# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.utils import timezone
#from db_file_storage.model_utils import delete_file, delete_file_if_needed




class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    actie_naam = models.CharField(max_length=150, default='-')
    actie_aanmaakdatum = models.DateField(null=False, blank=False, default=timezone.now)
    actie_einddatum = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    actie_eindtijdstip = models.TimeField(default='00:00:00')
    actie_gebruiker = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


