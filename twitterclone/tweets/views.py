from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from twitterclone.tweets.forms import TweetForm
from twitterclone.tweets.models import Tweet
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.notifications.models import Notification
import re

@login_required
def tweets(request):
    html = "index.html"
    following = request.user.twitteruser.follows.all()
    tweets = Tweet.objects.filter(author=request.user.twitteruser)
    following_tweets = Tweet.objects.filter(author__in=following)
    boffum = tweets | following_tweets
    notification_count = Notification.objects.filter(user=request.user.twitteruser).count()
    return render(request, html, {
        'tweets': boffum,
        'notification_count': notification_count
        })

# Alec helped with Notifications portion
@login_required
def add_tweet_view(request):
    html = "generic_form.html"
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(
                content=data['content'],
                author=request.user.twitteruser
                )
            if '@' in data['content']:
                other_users = re.findall(r'@(\w+)', data['content'])
                for name in other_users:
                    tagged = TwitterUser.objects.get(user__username=name)
                    Notification.objects.create(
                        user=tagged,
                        tweet=new_tweet,
                    )
        return HttpResponseRedirect(reverse('homepage'))
    form = TweetForm()
    return render(request, html, {'form': form})

def tweet_view(request,id):
    html = "tweet.html"
    data = Tweet.objects.filter(id=id).first()
    author, content, post_date = data.author, data.content, data.post_date
    return render(request, html, {'data':data, 'author': author, 'content': content, 'post_date':post_date})