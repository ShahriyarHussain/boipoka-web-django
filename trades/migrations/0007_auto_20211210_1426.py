# Generated by Django 3.2.9 on 2021-12-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0006_auto_20211210_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
