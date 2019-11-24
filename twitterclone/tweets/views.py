from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from twitterclone.tweets.forms import TweetForm
from twitterclone.tweets.models import Tweet
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.notifications.models import Notification
import re


@login_required
def tweets(request):
    html = "tweets/tweets.html"
    tweets = Tweet.objects.all()
    # notif = Notification.objects.filter(user=request.user.twitteruser).count()
    # follow = list(request.user.twitteruser.follower.all())
    # tweets = []
    # for followee in follow:
    #     tweets = Tweet.objects.filter(user=followee)
    tweets = sorted(tweets, key=lambda tweet: tweet.post_time, reverse=True)
    return render(request, html, {
        'tweets': tweets,})


@login_required
def add_tweet_view(request):
    html = "tweets/generic_form.html"
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                content=data['content'],
                author=request.user.twitter_user
                )
            rege = re.findall(r'@(\w+)', data['content'])
            if rege:
                for thing in rege:
                    try:
                        author_find = TwitterUser.objects.get(twitter_user=thing)
                    except TwitterUser.DoesNotExist:
                        author_find = None
                    if author_find:
                        Notification.objects.create(
                            author=author_find,
                            content=new_tweet
                        )
            return HttpResponseRedirect(reverse('homepage'))
    return render(request, html, {'form': form})


def tweet_view(request,id):
    html = 'tweet.html'
    data = Tweet.objects.filter(id=id).first()
    author, tweet_content, post_time = data.author, data.content, data.post_time

    return render(request, html, {'data': data, 'author': author, 'tweet_content':tweet_content, 'post_time':post_time})
