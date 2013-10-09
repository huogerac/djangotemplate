# -*- coding: utf-8 -*-

def themes_processor(request):
    """ add themes variables to the templates """
    return {'THEMES_URL': 'themes/default/',
            'THEME_BASE': 'themes/default/base.html',
            'THEME_NAME': 'default',
           }





