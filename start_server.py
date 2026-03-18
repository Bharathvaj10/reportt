import os
import sys
import django
from django.core.management import execute_from_command_line

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
    try:
        # Run standard management command but with no-reload for stability
        sys.argv = ['manage.py', 'runserver', '127.0.0.1:8000', '--noreload', '--nothreading']
        execute_from_command_line(sys.argv)
    except Exception as e:
        with open('server_error.log', 'w') as f:
            import traceback
            traceback.print_exc(file=f)
        print(f"Server crashed: {e}")

if __name__ == "__main__":
    main()
