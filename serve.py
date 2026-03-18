import os
import sys
import faulthandler
faulthandler.enable()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')

import django
django.setup()

from django.core.handlers.wsgi import WSGIHandler
from waitress import serve

application = WSGIHandler()

if __name__ == "__main__":
    port = 8080
    print("=" * 50)
    print("HealthOrganizer - Stable Server (Waitress)")
    print(f"Access at: http://127.0.0.1:{port}/")
    print("=" * 50)
    serve(application, host='127.0.0.1', port=port, threads=1)
