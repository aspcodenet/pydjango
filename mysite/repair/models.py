from django.db import models

# Create your models here.
class Bokning(models.Model):
    regno = models.CharField(max_length=10)
    bokningstid = models.DateTimeField()
    beskrivning = models.CharField(max_length=200)
