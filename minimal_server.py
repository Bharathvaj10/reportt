import os
import sys
import django
from django.core.servers.basehttp import get_internal_wsgi_application
from wsgiref.simple_server import make_server

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
    try:
        django.setup()
        application = get_internal_wsgi_application()
        print("Starting Minimal Stable Server on http://127.0.0.1:8000")
        httpd = make_server('127.0.0.1', 8000, application)
        httpd.serve_forever()
    except Exception as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    main()
