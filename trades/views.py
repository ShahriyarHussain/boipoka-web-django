from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import AuthorSerializer, BookSerializer, ListingCommentSerializer, ListingSerializer, TradeSerializer
from .models import *
import requests
import json
# Create your views here.

base_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"


class ListingViewSet(viewsets.ModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    queryset = Trade.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class ListingCommentViewSet(viewsets.ModelViewSet):
    serializer_class = ListingCommentSerializer
    queryset = Listing_Comment.objects.all()


# class BookDetailsViews(generics.ListAPIView):
#     @api_view(['POST'])
#     def get_queryset(self, request):
#         isbn = request.data["isbn"]
#         bookDetails = requests(base_url+isbn)
#         if bookDetails == "<Response [200]":
#             bookDetails = bookDetails.text
#         else:
#             bookDetails = "No Data Found"

#         return Response(json.loads(bookDetails))
