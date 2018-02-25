# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Card, Game

admin.site.register(Card)
admin.site.register(Game)