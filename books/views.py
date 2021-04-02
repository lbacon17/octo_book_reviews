from django.shortcuts import render
from .models import Book, Category


def all_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/books.html', context)