from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Home Page')

def journal(request):
    return HttpResponse('Journal Page')

def about(request):
    return HttpResponse('About Page')