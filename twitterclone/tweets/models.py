from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from django.utils import timezone

class Tweet(models.Model):
    content = models.CharField(max_length=140, default='')
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    post_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author}\n {self.content}\n {self.post_time}'