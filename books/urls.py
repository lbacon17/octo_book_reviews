from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('<book_id>', views.book_details, name='book_details'),
]