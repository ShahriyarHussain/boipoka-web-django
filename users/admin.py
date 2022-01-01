from django.contrib import admin
from .models import Message, Profile, Report, Review

# Register your models here.
admin.site.register(Profile)
admin.site.register(Report)
admin.site.register(Review)
admin.site.register(Message)
