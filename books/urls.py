from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('<book_id>', views.book_details, name='book_details'),
    path('delete_review/<book_id>/<review_id>', views.delete_review, name='delete_review'),
    path('approve_review/<book_id>/<review_id>', views.approve_review, name='approve_review'),
]