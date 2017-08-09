# -*- coding: utf-8 -*-

import tweepy
from django.conf import settings
from django.core.management.base import BaseCommand

from twitter.serializers import TweetSerializer

auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        data = {"created_at": '2017-08-06 04:30:49', "favorite_count": status.favorite_count, "id_str": status.id_str,
                "source": status.source, "text": status.text, "user_description": status.user.description,
                "user_followers_count": status.user.followers_count, "user_id_str": status.user.id_str,
                "user_location": status.user.location, "user_name": status.user.name,
                "user_screen_name": status.user.screen_name, 'user_verified': status.user.verified}
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

    def on_error(self, status_code):
        if status_code == 420:
            return False


class Command(BaseCommand):
    help = "Start a Stream"

    def handle(self, **options):

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        myStream.filter(track=['SundayFunday'], async=True)
