from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def mainPage(request):
    return HttpResponse('Базовая страница сайта')