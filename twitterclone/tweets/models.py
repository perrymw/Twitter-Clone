from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from django.utils import timezone

class Tweet(models.Model):
    tweet = models.CharField(max_length=140),
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    post_time= models.DateTimeField(default=timezone.now)