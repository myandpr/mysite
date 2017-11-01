# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def index(request):
    return render(request,'home.html')
    #return HttpResponse("Hello,world.You`re at the app1 index.")
def ajax_cluster(request):
	if request.method == 'POST':
		if request.is_ajax():
			ip = request.POST.get('ip')
			#print(ip)
			dump = random.randrange(1, 68)
			disk_usage = random.randrange(1,56)
			cpu_load = random.randrange(1,56)
			cpu_rate = random.randrange(1,56)
			memory_usage = random.randrange(1,56)
			print(dump,disk_usage)
			ret = {"dump":dump, "disk_usage":disk_usage,"cpu_load":cpu_load,"cpu_rate":cpu_rate,"memory_usage":memory_usage}
			return JsonResponse(ret)
	return render(request, 'home.html')
