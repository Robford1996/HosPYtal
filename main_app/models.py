from django.db import models
from django.urls import reverse
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


def get_absolute_url(self):
    return reverse('detail', kwargs={'patient_id': self.id})


class Checkins(models.Model):
    date = models.DateField('Checked Date')
    time = models.TimeField('Checked Time')
    notes = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


def __str__(self):
    return f"{self.date} at {self.time} with notes: {self.notes}"


class Meta:
    ordering = ['-date']
