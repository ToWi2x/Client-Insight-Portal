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