import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()

try:
    print("Running makemigrations...")
    call_command('makemigrations', 'reports', interactive=False)
    print("Running migrate...")
    call_command('migrate', interactive=False)
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
