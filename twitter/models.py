# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tweet(models.Model):
    created_at = models.DateTimeField()
    favorite_count = models.IntegerField(default=0)
    id_str = models.CharField(max_length=300)
    source = models.CharField(max_length=300)
    text = models.CharField(max_length=300)

    user_description = models.CharField(max_length=300)
    user_followers_count = models.IntegerField(default=0)
    user_id_str = models.CharField(max_length=300)
    user_location = models.CharField(max_length=300)
    user_name = models.CharField(max_length=300)
    user_screen_name = models.CharField(max_length=300)
    user_verified = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.id)
