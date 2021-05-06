from django.db import models

# Create your models here.
class Deposit(models.Model):
    deposit = models.FloatField(max_length=40)
    term = models.FloatField(max_length=40)
    rate = models.FloatField(max_length=40)
    interest = models.FloatField(max_length=40)