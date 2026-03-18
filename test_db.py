import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib import admin
print("Admin imported")
# Accessing admin urls can trigger a lot of imports
try:
    from django.urls import resolve
    print("URL resolver imported")
except Exception as e:
    print(f"URL error: {e}")

from django.core.servers.basehttp import get_internal_wsgi_application
print("WSGI app imported")
app = get_internal_wsgi_application()
print("WSGI app initialized")

User = get_user_model()

try:
    print(f"User count: {User.objects.count()}")
except Exception as e:
    print(f"Error: {e}")
