from django.db import models
from django.contrib.auth.models import User

class ClientOutcome(models.Model):
    # Links each outcome row to a specific user/client account
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Information about the system outcomes
    project_name = models.CharField(max_length=200)
    system_uptime = models.FloatField(help_text="Uptime percentage (e.g., 99.9)")
    tickets_resolved = models.IntegerField(help_text="Total support tickets resolved this month")
    status = models.CharField(max_length=50, choices=[('Optimal', 'Optimal'), ('Action Required', 'Action Required')])
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.client.username} - {self.project_name}"
    

class DeviceHealth(models.Model):
    STATUS_CHOICES = [
        ('ONLINE', 'Online'),
        ('OFFLINE', 'Offline'),
        ('MAINTENANCE', 'Maintenance'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    device_name = models.CharField(db_index=True, max_length=100)
    device_type = models.CharField(max_length=50, default='Unknown') # e.g., 'CCTV', 'Firewall'
    location = models.CharField(max_length=100)     # e.g., 'Main Warehouse', 'Head Office'
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ONLINE')
    firmware_version = models.CharField(max_length=20, blank=True, null=True)
    last_ping = models.DateTimeField(auto_now=True) # Automatically updates on every save()

    def __str__(self):
        return f"{self.device_name} ({self.location})"
    
class SecurityAlert(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    severity = models.CharField(max_length=20, choices=[
        ('CRITICAL', 'Critical'), 
        ('WARNING', 'Warning'), 
        ('INFO', 'Info')
    ])
    alert_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.severity} - {self.alert_type}"