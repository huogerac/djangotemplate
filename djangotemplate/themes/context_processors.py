# -*- coding: utf-8 -*-
from django.conf import settings

def themes_processor(request):
    """ add themes variables to the templates """
    THEME_NAME = getattr(settings, 'THEME_NAME', 'default')
    return {'THEMES_URL': 'themes/%s/' % THEME_NAME,
            'THEME_BASE': 'themes/%s/base.html' % THEME_NAME,
            'THEME_NAME': THEME_NAME,
           }





