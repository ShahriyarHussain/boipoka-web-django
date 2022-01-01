from django.contrib import admin
from .models import Post, Post_Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Post_Comment)
