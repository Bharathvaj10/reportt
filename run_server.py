import os
import django
from django.core.handlers.wsgi import WSGIHandler
from waitress import serve

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()

def main():
    application = WSGIHandler()
    print("Starting Waitress server on http://127.0.0.1:8001")
    serve(application, host='127.0.0.1', port=8001)

if __name__ == "__main__":
    main()
