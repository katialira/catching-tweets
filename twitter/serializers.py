# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)

    created_at = serializers.CharField()
    favorite_count = serializers.IntegerField()
    id_str = serializers.CharField()
    source = serializers.CharField()
    text = serializers.CharField()

    user_description = serializers.CharField()
    user_followers_count = serializers.IntegerField()
    user_id_str = serializers.CharField()
    user_location = serializers.CharField()
    user_name = serializers.CharField()
    user_screen_name = serializers.CharField()
    user_verified = serializers.BooleanField()

    def create(self, validated_data):
        """Create and return a new Tweet."""
        return Tweet.objects.create(**validated_data)
