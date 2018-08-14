# -*- coding: utf-8 -*-

from project_name.settings import *

INSTALLED_APPS.append('lpg')

# MIDDLEWARE.insert(0, 'lpg.middleware.SimpleMiddleware')

ROOT_URLCONF = 'lpg.urls'

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
