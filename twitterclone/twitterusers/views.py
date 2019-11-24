from django.shortcuts import render
from twitterclone.twitterusers.forms import NewUserForm
from twitterclone.twitterusers.models import TwitterUser
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def profile(request):
    html = ".html"
    
    twitter_user = TwitterUser.objects.all()

    return render(request, html, {"twitter_user": twitter_user})

# help received from Alec
def new_user_view(request):
    html = 'tweets/generic_form.html'
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('user_name')
            password = form.cleaned_data.get('password')
            user = authenticate(
                username=username,
                password=password,
                )
            TwitterUser.objects.create(
                twitter_user=user
            )
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    form = NewUserForm()
    return render(request, html, {'form':form})

def follow_view(request, id):
    followuser = TwitterUser.objects.get(id=id)
    request.user.twitter_user.followers.add(followuser)
    return HttpResponseRedirect(reverse('profile', kwargs={'id': id}))


def unfollow_view(request, id):
    followuser = TwitterUser.objects.get(id=id)
    request.user.twitter_user.followers.remove(followuser)
    return HttpResponseRedirect(reverse('profile', kwargs={'id': id}))