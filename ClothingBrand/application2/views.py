from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def function1_app2(request):
    return HttpResponse("Hello, world from the second application! hopin i find the ")

def function2_app2(request):
    return HttpResponse("Hello, world from the second function of the second application!")

def renderhtmlrequest(request):
    name = {'name': 'ABC'}
    return render(request, 'application2/homeofapp2.html',context=name)

def renderhtmlrequest2(request):
    return render(request, 'application2/homeofapp2.html', {"name":"HTML DJANGO"})

def filter_html(request):
    #return render(request, 'filters.html', {"filters":"HTML DJANGO"})
    #return render(request, 'filters.html') pass hola     
    #return render(request, 'filters.html', {"filters":"html django"})
    d = datetime.now()
    students = {'names': {'Ram','Raman','Rakesh','Rajesh','Rana'}}
    return render(request, 'filters.html',{'filters': d , 'nm': 1, 'names': students['names']})