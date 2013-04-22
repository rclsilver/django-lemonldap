from django.conf import settings
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render

def debug(request):
    if not settings.DEBUG:
        raise SuspiciousOperation("This view isn't available in production mode! Please set DEBUG to True")
    auth_headers = {}
    auth_headers['username'] = request.META.get('HTTP_AUTH_USER', None)
    auth_headers['groups'] = request.META.get('HTTP_AUTH_GROUPS', '').split('; ')
    auth_headers['is_superuser'] = request.META.get('HTTP_AUTH_SUPERUSER', None) == 'true'
    auth_headers['is_staff'] = request.META.get('HTTP_AUTH_STAFF', None) == 'true'
    return render(request, 'lemonldap/debug.html', {'auth_headers': auth_headers})
