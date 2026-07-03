from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ClientOutcome, SecurityAlert, DeviceHealth  # <-- We must import all 3 models!

@login_required(login_url='/accounts/login/')
def client_dashboard(request):
    # 1. Grab all data assigned to the person currently logged in
    outcomes = ClientOutcome.objects.filter(client=request.user)
    alerts = SecurityAlert.objects.filter(client=request.user, is_resolved=False).order_by('-timestamp')
    devices = DeviceHealth.objects.filter(client=request.user)
    
    # 2. Count the alerts so Chart.js knows how big to draw the slices
    critical_count = alerts.filter(severity='CRITICAL').count()
    warning_count = alerts.filter(severity='WARNING').count()
    info_count = alerts.filter(severity='INFO').count()
    
    # 3. Package ALL of this data together to send to the HTML template
    context = {
        'outcomes': outcomes,
        'alerts': alerts,
        'devices': devices,
        'critical_count': critical_count,
        'warning_count': warning_count,
        'info_count': info_count,
    }
    return render(request, 'dashboard/client_dashboard.html', context)