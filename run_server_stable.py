import os
import django
from django.core.handlers.wsgi import WSGIHandler
from wsgiref.simple_server import make_server

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()

def main():
    application = WSGIHandler()
    print("Serving on http://127.0.0.1:8000 (Stable Standard Server)")
    with make_server('127.0.0.1', 8000, application) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    main()
