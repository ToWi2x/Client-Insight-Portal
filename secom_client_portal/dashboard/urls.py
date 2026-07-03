from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_dashboard, name='dashboard'),
    path('api/device-ping/', views.device_ping_api, name='device_ping_api'),
]