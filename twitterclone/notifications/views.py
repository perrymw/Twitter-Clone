from django.shortcuts import render
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.notifications.models import Notification
from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def notificationpage(request):
    html = 'notifications.html'
    data = Notification.objects.filter(user=request.user.twitteruser)
    for thing in data:
        thing.delete()
    return render(request, html, {'data': data}) 