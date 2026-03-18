import os
import django
import faulthandler

faulthandler.enable()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()

from django.contrib.auth import get_user_model
from reports.models import MedicalReport, Reminder

def diagnostic():
    try:
        print("Checking Database Connection...")
        User = get_user_model()
        user_count = User.objects.count()
        print(f"User count: {user_count}")
        
        print("Checking Reports...")
        report_count = MedicalReport.objects.count()
        print(f"Report count: {report_count}")
        
        print("Checking Reminders...")
        reminder_count = Reminder.objects.count()
        print(f"Reminder count: {reminder_count}")
        
        print("Diagnostic finished successfully!")
    except Exception as e:
        print(f"Diagnostic failed with error: {e}")

if __name__ == "__main__":
    diagnostic()
