from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponseRedirect, reverse, HttpResponse
from django.utils import timezone
from twitterclone.authentication.forms import LoginForm, SignUpForm


def login_view(request):
    html = "generic_form.html"

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            if user := authenticate(
                username=data['username'],
                password=data['password']
            ):
                login(request, user)
                # breakpoint()
                return HttpResponseRedirect(request.GET.get('next', '/'))

    return render(request, html, {'form': form})


def sign_up_view(request):
    html = "generic_form.html"
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(
                username=data['username'],
                password=data['password']
                )
            if user := authenticate(
                username=data['username'],
                password=data['password']
            ):
                login(request, user)
            return HttpResponseRedirect(reverse('homepage'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
    return render(request, html, {'form': form})