# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Comment


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('title','published_date','author')
	search_fields = ('title','author','content')


class HandleComment(admin.ModelAdmin):
	list_display = ('post','author','created_date','approved_comment')
	search_fields = ('post','author')

admin.site.register(Post, AuthorAdmin)
admin.site.register(Comment, HandleComment)