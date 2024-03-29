"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitterclone.tweets.models import Tweet
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.notifications.models import Notification
from twitterclone.authentication.urls import urlpatterns as auth_urls
from twitterclone.notifications.urls import urlpatterns as notif_urls
from twitterclone.tweets.urls import urlpatterns as tweet_urls
from twitterclone.twitterusers.urls import urlpatterns as user_urls

admin.site.register(Tweet)
admin.site.register(TwitterUser)
admin.site.register(Notification)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += auth_urls
urlpatterns += notif_urls
urlpatterns += tweet_urls
urlpatterns += user_urls
