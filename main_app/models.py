from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Medication(models.Model):
    name = models.CharField(max_length=50)
    use = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('medication_detail', kwargs={'pk': self.id})


class Patient(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    reason = models.TextField(max_length=250)
    checkin = models.DateField()
    medication = models.ManyToManyField(Medication)
    users = models.ForeignKey(User, on_delete=models.CASCADE)


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


class Photo(models.Model):
    url = models.CharField(max_length=200)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for patient_id: {self.patient_id} @{self.url}"
