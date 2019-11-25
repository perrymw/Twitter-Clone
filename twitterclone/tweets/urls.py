from django.contrib import admin
from django.urls import path
from twitterclone.tweets import views
from twitterclone.tweets.models import Tweet


urlpatterns = [
    path('', views.tweets, name='homepage'),
    path('addtweet/', views.add_tweet_view, name='add_tweet'),
    path('tweet/<int:id>/', views.tweet_view, name='tweet')
    ]