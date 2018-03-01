# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('title','published_date','author')
	search_fields = ('title','author','content')


admin.site.register(Post, AuthorAdmin)
