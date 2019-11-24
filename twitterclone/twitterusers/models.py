from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
    twitter_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="twitter_user", null=True)
    followers = models.ManyToManyField('self', default=None, related_name='follow', blank=True,symmetrical=False)

    def __str__(self):
        return f'{self.twitter_user}'
    
