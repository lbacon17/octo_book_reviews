from django.shortcuts import render, get_object_or_404
from .models import Book, Category


def all_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/books.html', context)


def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    template = 'books/book_details.html'
    context = {
        'book': book,
    }
    return render(request, template, context)
