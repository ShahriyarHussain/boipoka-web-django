from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.

genres = [
    ('Fantasy', 'Fantasy'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Action & Adventure', 'Action & Adventure'),
    ('Mystery', 'Mystery'),
    ('Horror', 'Horror'),
    ('Thriller', 'Thriller'),
    ('Romance', 'Romance'),
    ('Biography', 'Biography'),
    ('Science & Technology', 'Science & Technology'),
    ('Humor', 'Humor'),
    ('History', 'History'),
    ('Children', 'Children'),
    ('Travel', 'Travel'),
]

negotiable_choices = [
    (True, 'Yes'),
    (False, 'No')
]

listing_choices = [
    (True, 'Sell'),
    (False, 'Exchange')
]

condition_choices = [
    (1, 'Excellent'),
    (2, 'Fair'),
    (3, 'Acceptable'),
    (4, 'Well Worn'),
    (5, 'Poor'),
]


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    isbn = models.CharField(unique=True, blank=False,
                            max_length=100, null=False)
    description = models.TextField(blank=True, null=False)
    genres = models.CharField(max_length=25, choices=genres)
    pages = models.IntegerField(blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)
    author = models.ManyToManyField(Author, blank=False)
    # author = models.CharField(blank=False, max_length=500, null=True)
    image = models.ImageField(
        blank=True, upload_to='book_covers', default='default.png')

    def __str__(self):
        return f'{self.title}'

    # def save(self):
    #     super().save


class Listing(models.Model):
    descriptions = models.CharField(max_length=1000, blank=True)
    price = models.IntegerField(blank=False, default=0)
    condition = models.IntegerField(choices=condition_choices, blank=False)
    negotiable = models.BooleanField(
        default=False, choices=negotiable_choices, blank=False)
    listing_type = models.BooleanField(
        default=False, blank=False, choices=listing_choices)
    date = models.DateTimeField(default=timezone.now)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='listed_book')
    options = models.ManyToManyField(
        Book, related_name='suggested_books', null=True)
    listed_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='adds_listing', blank=False, null=False)
    wishlisted_by = models.ManyToManyField(
        User, related_name='wishlists', blank=True)
    viewed_by = models.ManyToManyField(
        User, related_name='views', blank=True)
    trades = models.ManyToManyField(
        User, related_name='trades', through='Trade', blank=True)

    if listing_type:
        options = None
    else:
        negotiable = None
        price = -1

    def __str__(self):
        return f'{self.listed_by}\'s listing'

    class Meta:
        ordering = ['-date']

    # def save(self, *args, **kwargs):
    #     super().save


class Listing_Image(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='listing_images', blank=True, default='https://mir-s3-cdn-cf.behance.net/project_modules/1400/56d96263885635.5acd0047cf3e6.jpg')

    def __str__(self):
        return f'{self.listing.listed_by}--{self.listing.book.title}\'s listing image'


class Trade(models.Model):
    tradee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tradee')
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="listing")
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.listing.book.title}|{self.tradee}-{self.listing.listed_by}'


class Listing_Comment(models.Model):
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, blank=False, null=True)
    comment_date = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f'{self.commenter}\'s comment on {self.listing.listed_by.username}\'s listing'
