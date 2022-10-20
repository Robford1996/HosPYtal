from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('patients/', views.patients_index, name='index'),
    path('patients/<int:patient_id>/', views.patients_detail, name='detail'),
]
