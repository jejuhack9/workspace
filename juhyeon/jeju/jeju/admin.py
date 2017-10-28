# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *


from django.contrib import admin
from .models import Searchedkey, Foods, Reply, Corporation

admin.site.register(Searchedkey)
admin.site.register(Foods)
admin.site.register(Reply)
admin.site.register(Corporation)
