from django.conf import settings
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render
from lemonldap.auth.middleware import LemonldapAuthenticationMiddleware

def debug(request):
    if not settings.DEBUG:
        raise SuspiciousOperation("This view isn't available in production mode! Please set DEBUG to True")
    auth_headers = {}
    for header in LemonldapAuthenticationMiddleware.headers:
        auth_headers[header[0]] = request.META.get(header[1], None)
    return render(request, 'lemonldap/debug.html', {'auth_headers': auth_headers})
