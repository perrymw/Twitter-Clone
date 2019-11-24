from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput())
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput())
    user_name = forms.CharField(required=True, widget=forms.widgets.TextInput())
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput())

    class Meta:
        fields = [
            'first_name',
            'last_name',
            'user_name',
            'password',
        ]
        model = User