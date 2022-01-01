# Generated by Django 3.2.9 on 2021-12-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('Sale', 'Is Having A Sale'), ('Giveaway', 'Is Performing A Giveaway'), ('Post Share', 'Shared A Post!'), ('Book Review', 'Has Shared A Book Review!'), ('Reading New Book', 'Is Reading A New Book!')], default='Shared A Post', max_length=30),
        ),
    ]
