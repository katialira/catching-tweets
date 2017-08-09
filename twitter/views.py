# -*- coding: utf-8 -*-

from rest_framework import viewsets, filters
from .models import Tweet
from .serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tweet.objects.all().order_by('-created_at')
    serializer_class = TweetSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('user_name',)
