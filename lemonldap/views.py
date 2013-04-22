from django.conf import settings
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render

def debug(request):
    if not settings.DEBUG:
        raise SuspiciousOperation("This view isn't available in production mode! Please set DEBUG to True")
    return render(request, 'lemonldap/debug.html')
