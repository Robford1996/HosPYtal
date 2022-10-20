from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    reason = models.TextField(max_length=250)
    checkin = models.DateField()


def __str__(self):
    return self.name
