from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('patients/', views.patients_index, name='index'),
    path('patients/<int:patient_id>/', views.patients_detail, name='detail'),
    path('patients/create/', views.PatientCreate.as_view(), name='patients_create'),
    path('patients/<int:pk>/update/',
         views.PatientUpdate.as_view(), name='patients_update'),
    path('patients/<int:pk>/delete/',
         views.PatientDelete.as_view(), name='patients_delete'),
    path('patients/<int:patient_id>/add_checkins/',
         views.add_checkins, name='add_checkins'),
    path('medication/', views.MedicationList.as_view(), name='medication_index'),
    path('medication/<int:pk>', views.MedicationDetail.as_view(),
         name='medication_detail'),
    path('medication/create/', views.MedicationCreate.as_view(),
         name='medication_create'),
    path('medication/<int:pk>/update',
         views.MedicationUpdate.as_view(), name='medication_update'),
    path('medication/<int:pk>/delete',
         views.MedicationDelete.as_view(), name='medication_delete'),
    path('patients/<int:patient_id>/assoc_medication/<int:medication_id>/',
         views.assoc_medication, name='assoc_medication'),
    path('patients/<int:patient_id>/add_photo',
         views.add_photo, name='add_photo'),
]
