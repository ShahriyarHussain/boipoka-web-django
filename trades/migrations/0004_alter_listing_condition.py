# Generated by Django 3.2.9 on 2021-12-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0003_auto_20211210_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Excellent'), (2, 'Fair'), (3, 'Acceptable'), (4, 'Well Worn'), (5, 'Poor')]),
        ),
    ]