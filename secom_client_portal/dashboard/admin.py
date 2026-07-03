from django.contrib import admin
from .models import ClientOutcome, SecurityAlert, DeviceHealth

@admin.register(ClientOutcome)
class ClientOutcomeAdmin(admin.ModelAdmin):
    list_display = ('client', 'project_name', 'system_uptime', 'tickets_resolved', 'status', 'last_updated')
    list_filter = ('status', 'client')

@admin.register(SecurityAlert)
class SecurityAlertAdmin(admin.ModelAdmin):
    list_display = ('client', 'severity', 'alert_type', 'location', 'timestamp', 'is_resolved')
    list_filter = ('severity', 'is_resolved') 

@admin.register(DeviceHealth)
class DeviceHealthAdmin(admin.ModelAdmin):
    list_display = ('client', 'device_name', 'location', 'status', 'last_ping')
    list_filter = ('status', 'location')       