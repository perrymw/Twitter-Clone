from django.shortcuts import render
from twitterclone.tweets.forms import Tweet

def index(request):
    html = "index.html"
    
    tweet = Tweet.objects.all()

    return render(request, html, {"data": tweet})

def tweet_view(request, id):
    html = in
