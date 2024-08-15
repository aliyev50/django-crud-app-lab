from django.shortcuts import render

from django.http import HttpResponse


class Book:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


books = [
    Book('Power', 'Personal Success', 8 ),
    Book('Atomic Habits', 'Help lead to an improved life', 9 ),
    
]


def home(request):
    return HttpResponse('<h1>Welcome to Book App</h1>')

def about(request):
    return render(request, 'about.html')


def book_index(request):
    return render(request, 'books/index.html', {'books': books})