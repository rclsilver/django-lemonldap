#!/usr/bin/python

from distutils.core import setup
from lemonldap import __version__

setup(
    name='django-lemonldap',
    version=__version__,
    description='LemonLDAP: django authentication system to be used with LemonLDAP::NG',
    long_description='LemonLDAP: Allow users to be authenticated through LemonLDAP::NG in django applications',
    author='Thomas Betrancourt',
    author_email='thomas@betrancourt.net',
    url='https://github.com/rclsilver/django-lemonldap',
    packages=[
        'lemonldap',
        'lemonldap.auth',
    ],
)

