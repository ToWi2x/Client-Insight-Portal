import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ClientOutcome, SecurityAlert, DeviceHealth  

@login_required
def client_dashboard(request):
    outcomes = ClientOutcome.objects.filter(client=request.user)
    alerts = SecurityAlert.objects.filter(client=request.user, is_resolved=False).order_by('-timestamp')
    devices = DeviceHealth.objects.filter(client=request.user)
    
    # 2. Count the alerts so Chart.js knows how big to draw the slices
    critical_count = alerts.filter(severity='CRITICAL').count()
    warning_count = alerts.filter(severity='WARNING').count()
    info_count = alerts.filter(severity='INFO').count()

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


@csrf_exempt  
def device_ping_api(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Only POST is allowed.'}, status=405)

    try:
        payload = json.loads(request.body)
        
        device_id = payload.get('device_id')
        reported_status = payload.get('status', 'ONLINE').upper()
        firmware = payload.get('firmware_version')

        # Locate the specific hardware node in our database
        device = DeviceHealth.objects.get(id=device_id)

        # Modify the database row with the live hardware telemetry
        device.status = reported_status
        if firmware:
            device.firmware_version = firmware
        
        device.save()

        return JsonResponse({
            'status': 'success',
            'message': f'Handshake complete. Sync successful for {device.device_name}.'
        }, status=200)

    except DeviceHealth.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Device not found.'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Malformed payload.'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)