from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
    twitter_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="twitter_user", null=True),
    followers = models.ManyToManyField(User, default=None, related_name='follow', blank=True),
