from django.db import models

# Create your models here.
class AppDB(models.Model):
    tidspunkt = models.CharField(max_length=75, default="")
    tid = models.CharField(max_length=75, default="")
    intervall = models.CharField(max_length=75, default="")
    tid_siden_siste = models.CharField(max_length=75, default="")
    pod_navn = models.CharField(max_length=75, default="")