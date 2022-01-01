# from django.shortcuts import render
# from users.models import Profile
from datetime import datetime
from django.db.models import query
from .serializers import CommentSerializer, LikesSerializer, PostSerializer
from .models import Post, Post_Comment
# from rest_framework import viewsets
from rest_framework import viewsets
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class LikesViewSet(viewsets.ModelViewSet):
    serializer_class = LikesSerializer
    queryset = Post.objects.all()


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Post_Comment.objects.all()


# class PostDetailsAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
