from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(forms.Form):
    first_name = forms.CharField(required=True,
                                widget=forms.widgets.TextInput(
                                    attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True,
                                widget=forms.widgets.TextInput(
                                    attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(widget=forms.widgets.TextInput(
                                    attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(
                                    attrs={'placeholder': 'Password'}))