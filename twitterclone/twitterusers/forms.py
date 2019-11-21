from django import forms
from twitterclone.twitterusers.models import TwitterUser


class TwitterUserForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = [
            'username'
        ]