import os
import django
import faulthandler

faulthandler.enable()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_report_system.settings')
django.setup()

from django.test import Client

def test_request():
    print("Simulating internal GET request to /accounts/dashboard/...")
    client = Client()
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        user, _ = User.objects.get_or_create(username='testuser')
        client.force_login(user)
        
        response = client.get('/accounts/dashboard/')
        print(f"Response status: {response.status_code}")
        if response.status_code == 200:
            print("SUCCESS: Dashboard accessed successfully!")
        else:
            print(f"FAILED: Dashboard returned {response.status_code}")
            # Try to see if there's a traceback or error message in content
            if hasattr(response, 'content'):
                print(f"Error content first 500 chars: {response.content[:500]}")
            
    except Exception as e:
        print(f"Internal request failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_request()
