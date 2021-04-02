from django.contrib import admin
from .models import Book, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


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
admin.site.register(Category, CategoryAdmin)
