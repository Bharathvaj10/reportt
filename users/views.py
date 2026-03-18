from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from reports.models import NotificationLog

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome to HealthOrganizer!")
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard_view(request):
    recent_reports = request.user.reports.all().order_by('-upload_date')[:5]
    reminders = request.user.reminders.filter(is_active=True).order_by('time')
    emergency_contacts = request.user.emergency_contacts.all()
    recent_notifications = request.user.notifications.all().order_by('-created_at')[:5]
    
    context = {
        'recent_reports': recent_reports,
        'reminders': reminders,
        'emergency_contacts': emergency_contacts,
        'recent_notifications': recent_notifications,
        'has_reports': request.user.reports.exists(),
    }
    return render(request, 'users/dashboard.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')
