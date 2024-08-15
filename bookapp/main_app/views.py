from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Welcome to Book App</h1>')

def about(request):
    return HttpResponse('<h1>About the Book</h1>')
