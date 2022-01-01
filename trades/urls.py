from django.contrib.auth.models import update_last_login
from django.db import router
from django.urls import path
from django.urls.conf import include, re_path

from .views import *
from rest_framework import routers

listing_router = routers.SimpleRouter()
book_router = routers.SimpleRouter()
trade_router = routers.SimpleRouter()
author_router = routers.SimpleRouter()
listing_comment_router = routers.SimpleRouter()
# book_details_router = routers.SimpleRouter()

listing_router.register(r'listings', ListingViewSet)
book_router.register(r'books', BookViewSet)
trade_router.register(r'trades', TradeViewSet)
author_router.register(r'authors', AuthorViewSet)
listing_comment_router.register(r'listing_comments', ListingCommentViewSet)
# book_details_router.register(r'book_details/', BookDetailsViewSet)

urlpatterns = [
    path('', include(listing_router.urls)),
    path('', include(book_router.urls)),
    path('', include(trade_router.urls)),
    path('', include(author_router.urls)),
    path('', include(listing_comment_router.urls)),
    # re_path('^book_details/(?P<isbn>.+)/$', BookDetailsViews.as_view()),
]
