import os
import django
import faulthandler

faulthandler.enable()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()

from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

def test_auth_objects():
    print("Testing AnonymousUser instantiation...")
    user = AnonymousUser()
    print(f"AnonymousUser created: {user}")
    
    print("Testing User model instantiation...")
    User = get_user_model()
    temp_user = User(username='test_temp')
    print(f"User object created: {temp_user}")
    
    print("Success!")

if __name__ == "__main__":
    test_auth_objects()
