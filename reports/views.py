from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MedicalReport, Medicine, Reminder, EmergencyContact, NotificationLog
from .forms import MedicalReportForm, ReminderForm, EmergencyContactForm
from django.core.mail import send_mail
from django.conf import settings

def send_notification(user, reminder):
    """
    Sends an email reminder and logs it to the database.
    """
    target = reminder.contact_info or getattr(user, 'email', '')
    message = f"Reminder for {reminder.medicine_name}. Take {reminder.dosage_count} unit(s) at {reminder.time}."
    
    # 1. Log to database
    log = NotificationLog.objects.create(
        user=user,
        notification_type='Email',
        target=target,
        message=message,
        status='Pending'
    )
    
    # 2. Send email
    try:
        send_mail(
            subject=f"HealthOrganizer: {reminder.medicine_name} Reminder",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[target],
            fail_silently=False,
        )
        log.status = 'Sent'
        print(f"EMAIL SENT: To {target}")
    except Exception as e:
        log.status = f'Logged (Email config needed)'
        print(f"EMAIL LOG: [{target}] {message} (Setup needed: {e})")
    
    log.save()
    return True

@login_required
def report_list(request):
    reports = MedicalReport.objects.filter(user=request.user).order_by('-upload_date')
    return render(request, 'reports/list.html', {'reports': reports})

@login_required
def upload_report(request):
    if request.method == 'POST':
        form = MedicalReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            
            # Simple Keyword-based Categorization Fallback
            text_context = f"{report.title} {report.doctor_name} {report.hospital_name}".lower()
            if "blood" in text_context or "test" in text_context:
                report.category = "Blood Test"
            elif "tablet" in text_context or "capsule" in text_context or "prescription" in text_context:
                report.category = "Prescription"
            elif "scan" in text_context or "mri" in text_context or "x-ray" in text_context:
                report.category = "Scan Report"
            elif "discharge" in text_context:
                report.category = "Discharge Summary"
            report.save()

            messages.success(request, f"Report '{report.title}' uploaded successfully and categorized as {report.category}.")
            return redirect('report_detail', pk=report.pk)
    else:
        form = MedicalReportForm()
    return render(request, 'reports/upload.html', {'form': form})

@login_required
def report_detail(request, pk):
    report = get_object_or_404(MedicalReport, pk=pk, user=request.user)
    return render(request, 'reports/detail.html', {'report': report})

@login_required
def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.notification_method = 'Email'
            reminder.save()
            
            # Send email notification
            send_notification(request.user, reminder)
            
            messages.success(request, f"Medication reminder for {reminder.medicine_name} set successfully. Notification logged.")
            return redirect('dashboard')
    else:
        form = ReminderForm()
    return render(request, 'reports/add_reminder.html', {'form': form})

@login_required
def emergency_info(request):
    contacts = EmergencyContact.objects.filter(user=request.user)
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request, "Emergency contact added.")
            return redirect('emergency_info')
    else:
        form = EmergencyContactForm()
    return render(request, 'reports/emergency.html', {'contacts': contacts, 'form': form})
