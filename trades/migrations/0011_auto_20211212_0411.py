# Generated by Django 3.2.9 on 2021-12-12 04:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trades', '0010_alter_book_genres'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listing_Comments',
            new_name='Listing_Comment',
        ),
        migrations.RenameModel(
            old_name='Listing_Images',
            new_name='Listing_Image',
        ),
    ]
