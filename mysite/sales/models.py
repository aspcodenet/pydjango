from django.db import models

# Create your models here.
class Car(models.Model):
    regno = models.CharField(max_length=10)
    salesstartdate = models.DateTimeField()
    price = models.IntegerField()