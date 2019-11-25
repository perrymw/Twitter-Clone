from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet
from django.contrib.auth.models import User


class Notification(models.Model):
    user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='notification_user')
    seen = models.BooleanField(default=False)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE,)
    def __str__(self):
        return f'{self.tweet.content} - {self.tweet.author}'