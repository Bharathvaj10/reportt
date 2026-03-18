import os
import django
from waitress import serve
from django.core.handlers.wsgi import WSGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()
application = WSGIHandler()

if __name__ == "__main__":
    print("Starting Waitress Server on http://127.0.0.1:8000")
    serve(application, host='127.0.0.1', port=8000, threads=2)
