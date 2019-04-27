from django import forms
from django.contrib.auth.models import User

from .models import Album, Song

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# class AlbumForm(forms.Form):
#
#     class Meta:
#         model = Album
#         fields = '__all__'
#
#
# class SongForm(forms.ModelForm):
#
#     class Meta:
#         model = Song
#         fields = ['song_title', 'file_type']
