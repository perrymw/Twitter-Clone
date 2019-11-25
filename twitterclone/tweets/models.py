from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from twitterclone.twitterusers.models import TwitterUser



class Tweet(models.Model):
    author = models.ForeignKey(TwitterUser, on_delete=models.DO_NOTHING, related_name='author')
    content = models.CharField(max_length=140)
    post_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-post_date', )


    def __str__(self):
        return f'{self.author} {self.content} {self.post_date}'