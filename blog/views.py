# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def contact(request):
	return render(request, 'blog/contact_me.html', {'fname': 'Abdulrasheed', 'lname': 'Ibrahim', 'country': 'Nigeria'})


def about(request):
	return render(request, 'blog/about.html', {'whatido': "I love coding django"})

# def	post_detail(request,pk):	
# 	post = get_object_or_404(Post, pk=pk)
# 	return	render(request,	'blog/post_detail.html', {'post': post})