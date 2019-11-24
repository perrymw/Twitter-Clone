from django.shortcuts import render
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.notifications.models import Notification
from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def notificationpage(request, id):
    html = 'notifications/notifications.html'
    twitteruser = TwitterUser.objects.filter(id=id).first()
    data = Notification.objects.filter(author=twitteruser)
    for thing in data:
        thing.delete()
    return render(request, html, {'data': data})    
