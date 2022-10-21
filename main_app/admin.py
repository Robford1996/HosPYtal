from django.contrib import admin
from .models import Patient, Checkins
# Register your models here.

admin.site.register(Patient)
admin.site.register(Checkins)
