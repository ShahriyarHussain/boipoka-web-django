# Generated by Django 3.2.9 on 2021-12-17 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_alter_post_post_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='liked_by',
        ),
    ]
