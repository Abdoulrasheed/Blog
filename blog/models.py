# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now
		self.save()


	def __str__(self):
		return self.title

class FeedBack(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	phone = models.PositiveIntegerField()
	content = models.TextField()
