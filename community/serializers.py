from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    # comments = CommentSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.liked_by.count()
        representation['commentCount'] = instance.comments.count()
        representation['author'] = instance.author.username
        return representation


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('liked_by', 'id')
