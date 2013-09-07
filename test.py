#!/usr/bin/env python

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'magictool.settings'

from notemanagement.models import Category

if __name__ == "__main__":
    cats = Category.objects.all()

    print cats