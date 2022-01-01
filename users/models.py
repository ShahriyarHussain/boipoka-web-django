from typing import Tuple
from django.contrib.auth.models import User
from django.db import models
from mapbox_location_field.models import LocationField
from django.utils import timezone
from PIL import Image
from trades.models import genres
# from django.core.validators import RegexValidator

default_map_attrs = {
    "style": "mapbox://styles/mapbox/outdoors-v11",
    "cursor_style": 'pointer',
    "marker_color": "red",
    "rotate": False,
    "geocoder": True,
    "fullscreen_button": True,
    "navigation_buttons": True,
    "track_location_button": True,
    "readonly": True,
    "placeholder": "Pick a location on map below",
    "language": "auto",
    "message_404": "undefined address", }

# Create your models here.


profile_genres = [
    ('Fantasy', 'Fantasy'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Action & Adventure', 'Action & Adventure'),
    ('Mystery', 'Mystery'),
    ('Horror', 'Horror'),
    ('Thriller', 'Thriller'),
    ('Romance', 'Romance'),
    ('Biography', 'Biography'),
    ('Science & Technology', 'Science & Technology'),
]


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=11, null=False,
                             blank=False, unique=True)
    image = models.ImageField(
        upload_to='profile_images', blank=True, default='default.png')

    days_logged_in = models.IntegerField(blank=False, default=1)
    favorite_genre = models.CharField(choices=genres, max_length=20)
    # location = LocationField(default=[(23.78091, 90.40756)])
    user_reports = models.ManyToManyField(
        'self', related_name='report', through='Report')
    user_reviews = models.ManyToManyField(
        'self', related_name='review', through='Review')
    user_messages = models.ManyToManyField(
        'self', related_name='send_message', through='Message')

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    # def save(self, *args, **kwargs):
    #     super().save()


class Report(models.Model):
    report_sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='report_sender')
    report_receiver = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='report_receiver')
    description = models.CharField(max_length=500, blank=False)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.report_sender.username} reported {self.report_receiver.username}'


class Review(models.Model):
    review_sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='review_sender')
    review_receiver = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='review_reciever')
    rating = models.IntegerField(blank=False)
    time = models.DateTimeField(blank=False, default=timezone.now)

    def __str__(self):
        return f'{self.reivew_sender.username} reviewed {self.review_receiver.username}'


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='message_sender')
    receiver = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='message_receiver')
    content = models.CharField(blank=False, max_length=500)
    time = models.DateTimeField(blank=False, default=timezone.now)
    attachment = models.ImageField(blank=True,
                                   upload_to='chat_uploads')

    def __str__(self):
        return f'{self.sender.user.username} messaged {self.receiver.user.username}'
