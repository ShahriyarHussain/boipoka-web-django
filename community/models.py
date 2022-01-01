from os import posix_fadvise
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

post_type = [
    ('Is Having A Sale', 'Is Having A Sale'),
    ('Is Performing A Giveaway', 'Is Performing A Giveaway'),
    ('Shared A Post!', 'Shared A Post!'),
    ('Has Shared A Book Review!', 'Has Shared A Book Review!'),
    ('Is Reading A New Book!', 'Is Reading A New Book!'),
]


class Post(models.Model):
    content = models.CharField(max_length=1000, blank=False)
    # image = models.ImageField(upload_to='post_images',
    #                           blank=True, default='default.png')
    date_posted = models.DateTimeField(default=timezone.now, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(
        User, blank=True, default=author, related_name='likes')
    comments = models.ManyToManyField(
        User, blank=True, related_name='comments', through='Post_Comment')
    post_type = models.CharField(
        max_length=30, blank=False, default='Post Share', choices=post_type)

    def __str__(self):
        return f'{self.author.username} post'

    class Meta:
        ordering = ['-date_posted']


class Post_Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return f'{self.commenter.username} comment'
