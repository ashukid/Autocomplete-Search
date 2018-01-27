# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=500)
	meta_data = models.CharField(max_length=1000)
	url = models.CharField(max_length=500)

	def __str__(self):
		return self.title


