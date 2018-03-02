# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms	import	PostForm
from django.utils import timezone


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def about(request):
	return render(request, 'blog/about.html', {'whatido': "I love coding django"})

def contact(request):
	return render(request, 'blog/contact_me.html', {'a': ''})
