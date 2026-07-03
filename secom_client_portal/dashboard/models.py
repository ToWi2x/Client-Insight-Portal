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
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    device_name = models.CharField(max_length=100, help_text="e.g., Loading Bay CCTV, Front Door Access")
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('ONLINE', 'Online'), ('OFFLINE', 'Offline'), ('MAINTENANCE', 'Maintenance')])
    last_ping = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device_name} - {self.status}"
    
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