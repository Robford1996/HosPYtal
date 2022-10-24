from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Medication, Photo
from .forms import CheckinsForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com'
BUCKET = 'hospytal'


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
    checkins_form = CheckinsForm()
    medication_patient_doesnt_have = Medication.objects.exclude(
        id__in=patient.medication.all().values_list('id'))
    return render(request, 'patients/detail.html', {
        'patient': patient,
        'checkins_form': checkins_form,
        'medication': medication_patient_doesnt_have,
    })


def add_checkins(request, patient_id):
    form = CheckinsForm(request.POST)
    if form.is_valid():
        new_checkins = form.save(commit=False)
        new_checkins.patient_id = patient_id
        new_checkins.save()
    return redirect('detail', patient_id=patient_id)


def assoc_medication(request, patient_id, medication_id):
    Patient.objects.get(id=patient_id).medication.add(medication_id)
    return redirect('detail', patient_id=patient_id)


def add_photo(request, patient_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}/{BUCKET}/{key}"
            photo = Photo(url=url, patient_id=patient_id)
            photo.save()
        except:
            print('An error occured uploading file to S3')
    return redirect('detail', patient_id=patient_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return (redirect('index'))
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class PatientCreate(CreateView):
    model = Patient
    fields = ['name', 'address', 'email', 'age', 'reason', 'checkin']
    success_url = '/patients/'

    def form_valid(self, form):
        form.instance.users = self.request.user
        return super().form_valid(form)


class PatientUpdate(UpdateView):
    model = Patient
    fields = ['name', 'age', 'reason']
    success_url = '/patients/'


class PatientDelete(DeleteView):
    model = Patient
    success_url = '/patients/'


class MedicationCreate(CreateView):
    model = Medication
    fields = ('name', 'use')


class MedicationUpdate(UpdateView):
    model = Medication
    fields = ('name', 'use')


class MedicationDelete(DeleteView):
    model = Medication
    success_url = '/medication/'


class MedicationDetail(DetailView):
    model = Medication
    template_name = 'medication/detail.html'


class MedicationList(ListView):
    model = Medication
    template_name = 'medication/index.html'
