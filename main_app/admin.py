from django.contrib import admin
from .models import Patient, Checkins, Photo, Medication
# Register your models here.

admin.site.register(Patient)
admin.site.register(Checkins)
admin.site.register(Photo)
admin.site.register(Medication)
