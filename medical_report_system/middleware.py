from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

class SafeAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.session.get('_auth_user_id')
        if user_id:
            try:
                User = get_user_model()
                request.user = User.objects.get(pk=user_id)
            except Exception:
                request.user = AnonymousUser()
        else:
            request.user = AnonymousUser()
        return self.get_response(request)
