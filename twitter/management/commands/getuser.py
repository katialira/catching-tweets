# -*- coding: utf-8 -*-

import tweepy
from django.conf import settings
from django.core.management.base import BaseCommand


auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_TOKEN_SECRET)


class Command(BaseCommand):
    help = "Get information of a certain user"

    def handle(self, **options):
        api = tweepy.API(auth)
        user = api.get_user('gvanrossum')
        print user.screen_name
        print user.followers_count
        for friend in user.friends():
            print friend.screen_name
