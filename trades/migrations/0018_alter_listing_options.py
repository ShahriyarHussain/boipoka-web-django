# Generated by Django 3.2.9 on 2021-12-31 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0017_book_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['-date']},
        ),
    ]