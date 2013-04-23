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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Natural Language :: French',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Session',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries',
    ],
    packages=[
        'lemonldap',
        'lemonldap.auth',
    ],
)

