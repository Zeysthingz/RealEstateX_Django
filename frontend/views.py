from django.http import HttpResponse
from django.shortcuts import render


# İÖ

def index(request):
    return HttpResponse('Hello World')
