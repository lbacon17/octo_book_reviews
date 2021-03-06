# Generated by Django 3.1.7 on 2021-03-31 23:16

import books.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('author', models.CharField(max_length=80)),
                ('published', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(books.models.Book.current_year)])),
                ('summary', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
        ),
    ]
