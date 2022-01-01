# Generated by Django 3.2.9 on 2021-12-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0015_auto_20211230_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='trades.Author'),
        ),
    ]
