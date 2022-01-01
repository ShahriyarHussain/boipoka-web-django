from typing import List
from rest_framework import serializers
from rest_framework.utils import representation
from .models import Author, Listing, Book, Listing_Comment, Trade
import requests


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['wishlisted_by'] = instance.wishlisted_by.all().count()
        representation['viewed_by'] = instance.viewed_by.all().count()
        representation['listed_by_names'] = instance.listed_by.username
        representation['book_name'] = instance.book.title

        return representation


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        authors = instance.author.all()
        names = []
        for singleAuthor in authors:
            names.append(singleAuthor.name)
        representation['author_names'] = names
        return representation


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ListingCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing_Comment
        fields = '__all__'
