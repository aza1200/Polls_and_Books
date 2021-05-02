"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
import site

from django.core.wsgi import get_wsgi_application
site.addsitedir('C:/Users/user/ch8_Apache/Lib/site-packages')

path = os.path.abspath(__file__+'/../..')
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
os.environ['DJANGO_SETTING_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
