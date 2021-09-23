from django.contrib import admin
from .models import Book, Category, Genre, Review, Rating


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class GenreAdmin(admin.ModelAdmin):
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


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'created_on',
        'approved',
    )

class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'score'
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Rating, RatingAdmin)
