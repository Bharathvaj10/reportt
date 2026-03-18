import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
try:
    count = User.objects.count()
    print(f"Database access SUCCESSFUL! User count: {count}")
except Exception as e:
    print(f"Database access FAILED: {e}")
