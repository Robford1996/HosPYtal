from django.shortcuts import render
# from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Patient


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


# class Patient:
#     def __init__(self, name, address, email, age, reason, checkin):
#         self.name = name
#         self.address = address
#         self.email = email
#         self.age = age
#         self.reason = reason
#         self.checkin = checkin


# patients = [
#     Patient('Mark Monday', '123 Sesame Street',
#             'MarkMon@gmail.com', 53, 'Heart Attack', '2022-10-10'),
#     Patient('Terry Tuesday', '45 Maryland Drive',
#             'TerryTues@gmail.com', 16, 'Broken Arm', '2022-10-16'),
#     Patient('Wanda Wednesday', '43 Jamison Way', 'WandaWed@gmail.com',
#             72, 'Lymphatic Cancer', '2022-9-30'),
# ]


def patients_index(request):
    patients = Patient.objects.all()
    return render(request, 'patients/index.html', {'patients': patients})


def patients_detail(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    return render(request, 'patients/detail.html', {'patient': patient})


class PatientCreate(CreateView):
    model = Patient
    fields = '__all__'
    success_url = '/patients/'
