from django.db import models

class Account(models.Model):
    acno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    password = models.CharField(max_length=30)


