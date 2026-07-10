from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.client_dashboard, name='dashboard'),
    path('api/device-ping/', views.device_ping_api, name='device_ping_api'),
]

