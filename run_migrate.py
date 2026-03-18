import os
import django
import faulthandler

faulthandler.enable()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()

from django.core.management import call_command

if __name__ == "__main__":
    print("Running makemigrations...")
    call_command('makemigrations')
    print("Running migrate...")
    call_command('migrate')
    print("Done!")
