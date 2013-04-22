from django.conf import settings
from django.conf.urls import patterns, url

urlpatterns = patterns('',
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^debug/?$', 'lemonldap.views.debug', name='debug'),
    )
