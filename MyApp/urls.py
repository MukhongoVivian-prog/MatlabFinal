
from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('doctors/', views.doctors, name='doctors'),
    path('departments/', views.department, name='departments'),
    path('appointments/', views.appointments, name='appointments'),
    path('show/', views.show, name='show'),

]

