from django.shortcuts import render

from .models import Book




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
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def book_index(request):
    books = Book.objects.all() 
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})