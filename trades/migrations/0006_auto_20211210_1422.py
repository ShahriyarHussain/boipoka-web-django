# Generated by Django 3.2.9 on 2021-12-10 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0005_auto_20211210_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='negotiable',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='price',
        ),
    ]