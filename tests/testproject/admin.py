# coding: utf-8
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from .models import Document, ParlerDocument

admin.site.register(Document)
admin.site.register(ParlerDocument)
