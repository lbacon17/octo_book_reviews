from django import forms
from .models import Book, Review


class BookForm(forms.ModelForm):

    class Meta:

        model = Book
        fields = ('category', 'genre', 'title', 'author', 
            'published', 'summary', 'price', 'rating', 
            'image_url', 'image',)


class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review
        fields = ('review_content',)
        exclude = ('book', 'created_on',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            placeholders = {
                'review_content': 'Leave your review here'
            }

            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
