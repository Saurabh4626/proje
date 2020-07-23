from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import json
# Create your views here.

data=[{'name':'saurabh','age':18},
		  {'name':'romil','age':12},
		  {'name':'rohan','age':28},
		  {'name':'sreyas','age':18},
		  {'name':'kajal','age':12},
		  {'name':'dudu','age':28}]

def url(request):
	return JsonResponse(data,safe=False)
name=[sub['name'] for sub in data]
age=[sub['age'] for sub in data]
print(str(name))
print(str(age))
dic={name[i]:age[i] for i in range(len(name))}
print(dic)

def home(request):
    return render(request,'home/home.html',{'dic':dic})
