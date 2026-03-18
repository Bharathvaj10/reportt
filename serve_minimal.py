import os
import sys
import faulthandler
faulthandler.enable()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')

import django
django.setup()

from django.core.servers.basehttp import WSGIServer, WSGIRequestHandler
from django.core.handlers.wsgi import WSGIHandler

def run_server():
    server_address = ('127.0.0.1', 8081)
    httpd = WSGIServer(server_address, WSGIRequestHandler)
    httpd.set_app(WSGIHandler())
    print(f"Server running at http://127.0.0.1:8081/")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
