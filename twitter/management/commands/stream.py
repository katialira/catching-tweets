# -*- coding: utf-8 -*-

import tweepy
from django.conf import settings
from django.core.management.base import BaseCommand


auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print status.text

    def on_error(self, status_code):
        if status_code == 420:
            return False


class Command(BaseCommand):
    help = "Start a Stream"

    def handle(self, **options):

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        myStream.filter(track=['SundayFunday'], async=True)
