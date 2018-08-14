# -*- coding: utf-8 -*-

import importlib

from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView

app_urls = importlib.import_module(settings.ORIGINAL_ROOT_URLCONF)

extra_patterns = [
    path('lpg/about/', TemplateView.as_view(template_name='lpg/about/index.html')),
]

urlpatterns = extra_patterns + app_urls.urlpatterns
