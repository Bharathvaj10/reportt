from django.db import models
from django.conf import settings

class MedicalReport(models.Model):
    CATEGORY_CHOICES = [
        ('Blood Test', 'Blood Test'),
        ('Prescription', 'Prescription'),
        ('Scan Report', 'Scan Report'),
        ('Discharge Summary', 'Discharge Summary'),
        ('General Report', 'General Report'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='reports/%Y/%m/%d/')
    extracted_text = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='General Report')
    doctor_name = models.CharField(max_length=255, blank=True)
    hospital_name = models.CharField(max_length=255, blank=True)
    report_date = models.DateField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title} ({self.category})"

class Medicine(models.Model):
    report = models.ForeignKey(MedicalReport, on_delete=models.CASCADE, related_name='medicines')
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100, blank=True)
    frequency = models.CharField(max_length=100, blank=True)
    instructions = models.TextField(blank=True)

    def __str__(self):
        return self.medicine_name

class Reminder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reminders')
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100, blank=True)
    dosage_count = models.PositiveIntegerField(default=1, help_text="Number of units to take")
    notification_method = models.CharField(max_length=10, default='Email')
    contact_info = models.CharField(max_length=255, default='', help_text="Email address for reminders")
    time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.medicine_name} at {self.time}"

class EmergencyContact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='emergency_contacts')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    relationship = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} ({self.relationship})"

class NotificationLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    notification_type = models.CharField(max_length=10, default='Email')
    target = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, default='Sent')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.target} at {self.created_at}"
