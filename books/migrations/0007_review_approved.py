# Generated by Django 3.2.7 on 2021-09-09 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
