# Generated by Django 3.2.9 on 2021-12-11 07:50

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_profile_favorite_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=mapbox_location_field.models.LocationField(default=[(23.78091, 90.40756)], map_attrs={}),
        ),
    ]