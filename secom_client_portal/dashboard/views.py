from django.shortcuts import render
from django.contrib.auth.decorators import login_required # <-- Check this import
from .models import ClientOutcome

@login_required(login_url='/accounts/login/')  # <-- This line MUST be right here
def client_dashboard(request):
    outcomes = ClientOutcome.objects.filter(client=request.user)
    context = {'outcomes': outcomes}
    return render(request, 'dashboard/client_dashboard.html', context)