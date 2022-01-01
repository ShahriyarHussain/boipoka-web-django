from django.contrib.auth.models import update_last_login
from django.urls import path
from django.urls.conf import include

from .views import *
from rest_framework import routers

post_router = routers.SimpleRouter()
likes_router = routers.SimpleRouter()
commnet_router = routers.SimpleRouter()

post_router.register(r'posts', PostViewSet)
likes_router.register(r'likes', LikesViewSet)
commnet_router.register(r'comments', CommentsViewSet)

urlpatterns = [
    path('', include(post_router.urls)),
    path('', include(likes_router.urls)),
    path('', include(commnet_router.urls)),
]
