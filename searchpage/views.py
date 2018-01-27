# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

from django.views import generic
from .models import *

class IndexView(generic.TemplateView):
	template_name = 'searchpage/index.html'


def search_query(request):
	query = request.GET['searchquery']
	article = Article.objects.all()
	current1 = article.filter(title__startswith=query)
	current2 = article.filter(meta_data__icontains=query)
	data1={}
	data2={}
	for i in range(len(current1)):
		data1[current1[i].title]=current1[i].url
	for i in range(len(current2)):
		data2[current2[i].title]=current2[i].url
	return JsonResponse({'data1':data1,'data2':data2})