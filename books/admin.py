from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'summary',
        'price',
        'rating',
    )

    ordering = ('title',)


admin.site.register(Book, BookAdmin)
