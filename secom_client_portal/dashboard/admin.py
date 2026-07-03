from django.contrib import admin
from .models import ClientOutcome

@admin.register(ClientOutcome)
class ClientOutcomeAdmin(admin.ModelAdmin):
    list_display = ('client', 'project_name', 'system_uptime', 'tickets_resolved', 'status', 'last_updated')
    list_filter = ('status', 'client')