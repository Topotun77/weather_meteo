"""
WSGI config for meteo_wt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import logging
import os
from .settings import DATA_DIR
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meteo_wt.settings')

application = get_wsgi_application()

logging.basicConfig(
        filename=os.path.join(DATA_DIR, 'weather_meteo.log'), filemode='a', encoding='utf-8',
        format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        level=logging.INFO)
