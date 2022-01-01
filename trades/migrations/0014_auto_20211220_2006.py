# Generated by Django 3.2.9 on 2021-12-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0013_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_type',
            field=models.BooleanField(choices=[(True, 'Sell'), (False, 'Exchange')], default=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='negotiable',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]