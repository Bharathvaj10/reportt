import os
import django
import faulthandler

faulthandler.enable()
print("Starting minimal setup test...")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()
print("Django setup SUCCESSFUL!")
