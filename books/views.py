from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Book, Category, Review
from .forms import BookForm, ReviewForm


def all_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/books.html', context)


def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = book.reviews.all()
    new_review = None
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.book = book
            new_review.save()
            messages.success(request, 'Your review was successfully submitted')
        else:
            messages.error(request, 'There was an issue submitting your review. Please ensure you have filled out all fields correctly')
    else:
        review_form = ReviewForm()
    template = 'books/book_details.html'
    context = {
        'book': book,
        'new_review': new_review,
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, template, context)
