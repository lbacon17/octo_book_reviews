from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.fields import DecimalField
import datetime


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Genre(models.Model):

    class Meta:
        verbose_name_plural = 'Genres'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Book(models.Model):

    class Meta:
        verbose_name_plural = 'Books'

    def current_year():
        return datetime.date.today().year

    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    genre = models.ForeignKey(Genre, null=True, blank=True, 
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=254, null=False, blank=False)
    author = models.CharField(max_length=80, null=False, blank=False)
    published = models.PositiveIntegerField(validators=[MinValueValidator(1900),
                                                MaxValueValidator(current_year)])
    summary = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5, null=False, 
                                blank=False, default=0.00)
    rating = models.DecimalField(decimal_places=2, max_digits=3, null=False,
                                 blank=False, default=0.00)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'

    book = models.ForeignKey(Book, null=False, blank=False, on_delete=models.CASCADE, related_name='reviews')
    review_content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.review_content


class Rating(models.Model):
    book = models.ForeignKey(Book, null=False, blank=False, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return str(self.pk)
