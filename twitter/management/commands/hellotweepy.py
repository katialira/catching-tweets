# -*- coding: utf-8 -*-

import tweepy
from django.conf import settings
from django.core.management.base import BaseCommand


auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)


class Command(BaseCommand):
    help = "Setup a simple tweet feed"

    def handle(self, **options):
        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print tweet.text
