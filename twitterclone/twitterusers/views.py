from django.shortcuts import render
from twitterclone.twitterusers.forms import NewUserForm
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet
from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views import View

# help received from Alec
class NewUserView(View):
    html = 'generic_form.html'
    def get(self, request):
        form = NewUserForm()
        return render(request, self.html, {'form': form})
    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                password=data['password'],
            )
            TwitterUser.objects.create(
                user=user,

            )
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        form = NewUserForm()
        return render(request, self.html, {'form': form})
    
    # Alec's help
class FollowView(View):
    @method_decorator(login_required)
    def get(self, request, username):
        current_user = request.user.twitteruser
        desired_user = User.objects.get(username=username)
        d_user_name = TwitterUser.objects.get(user=desired_user)
        current_user.follows.add(d_user_name)
        return HttpResponseRedirect(request.META.get('HTTP_REFFERER', '/'))

class UnfollowView(View):
    @method_decorator(login_required)
    def get(self, request, username):
        current_user = request.user.twitteruser
        desired_user = User.objects.get(username=username)
        d_user_name = TwitterUser.objects.get(user=desired_user)
        current_user.follows.remove(d_user_name)
        return HttpResponseRedirect(request.META.get('HTTP_REFFERER', '/'))

class ProfileView(View):
    html = 'profile.html'
    def get(self, request, username):
        user = User.objects.get(username=username)
        username = TwitterUser.objects.filter(user=user)
        tweets = Tweet.objects.filter(author=username.first())

        return render(request, self.html, {
            'user': user,
            'username': username,
            'tweets': tweets,
            })