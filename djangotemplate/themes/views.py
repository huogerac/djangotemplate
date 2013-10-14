# -*- coding: utf-8 -*-

import os

def get_themes():
    path = 'themes/templates/themes'
    if not path:
        return []
    layouts = [folder for folder in os.listdir(path)]
    layouts.sort()
    return layouts