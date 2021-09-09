from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    reviews = book.reviews.order_by('-created_on')
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


@login_required
def delete_review(request, review_id, book_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user.is_superuser:
        book = Book.objects.get(id=book_id)
        review.delete()
        messages.success(request, 'The review was successfully deleted.')
        return redirect(reverse('book_details', args=[book.id]))
    elif review.user == request.user:
        book = Book.objects.get(id=book_id)
        review.delete()
        messages.success(request, 'Your review was successfully deleted.')
        return redirect(reverse('book_details', args=[book.id]))
    else:
        messages.error(request, 'Sorry, you do not have permission to '
                       'perform that action.')
        return redirect(reverse('home'))