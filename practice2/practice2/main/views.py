from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def journal(request):
    return HttpResponse('Journal Page')

def about(request):
    return HttpResponse('About Page')

def student_list(request):
    students = ['Alice', 'Bob', 'Charlie', 'Diana']
    return render(request, 'main/student_list.html', {'students': students})