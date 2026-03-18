import os
import socket
import multiprocessing
import django
from django.core.handlers.wsgi import WSGIHandler
from wsgiref.simple_server import make_server, WSGIRequestHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')

def handle_request(conn, addr):
    # This runs in a fresh process
    django.setup()
    application = WSGIHandler()
    
    # Simple WSGI server for one request
    # We create a fake server object to satisfy wsgiref
    class SingleRequestServer:
        def __init__(self, conn, addr):
            self.conn = conn
            self.addr = addr
        def get_request(self):
            return self.conn, self.addr

    print(f"Handling request from {addr}...")
    try:
        from wsgiref.handlers import SimpleHandler
        handler = SimpleHandler(conn, conn, os.environ, sys.stderr)
        handler.run(application)
    except Exception as e:
        print(f"Error handling request: {e}")
    finally:
        conn.close()

import sys

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 8000))
    s.listen(5)
    print("Safe Multi-Process Server listening on http://127.0.0.1:8000")
    
    while True:
        try:
            conn, addr = s.accept()
            # Spawn a fresh process for EACH request to avoid memory corruption
            p = multiprocessing.Process(target=handle_request, args=(conn, addr))
            p.start()
            # Parent doesn't need the connection
            conn.close()
            # Wait a bit or clean up finished processes
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Server loop error: {e}")

if __name__ == "__main__":
    multiprocessing.freeze_support() # For Windows
    main()
